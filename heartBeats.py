import time
from ISStreamer.Streamer import Streamer
import adafruit_ads1x15


if __name__ == '__main__':

    streamer = Streamer(bucket_name="demo",bucket_key="MP5C4E8FD3VS",access_key="ist_VyBltj0nrsQHMzsAQVwFVSnqj4MIea_9")

    adc = adafruit_ads1x15.ADS1115() 
    GAIN = 2/3  
    curState = 0
    thresh = 525  
    P = 512
    T = 512
    stateChanged = 0
    sampleCounter = 0
    lastBeatTime = 0
    firstBeat = True
    secondBeat = False
    Pulse = False
    IBI = 600
    rate = [0]*10
    amp = 100
    z = 0

    lastTime = int(time.time()*1000)

   
    while True:
        
        Signal = adc.read_adc(0, gain=GAIN)   
        curTime = int(time.time()*1000)

        sampleCounter += curTime - lastTime;       
        lastTime = curTime
        N = sampleCounter - lastBeatTime;     
      
       
        if Signal < thresh and N > (IBI/5.0)*3.0 : 
            if Signal < T :                        
              T = Signal;                         
        if Signal > thresh and  Signal > P:           
            P = Signal;                            
                                                
        if N > 250 :                                   
            if  (Signal > thresh) and  (Pulse == False) and  (N > (IBI/5.0)*3.0)  :       
              Pulse = True;                               # set the Pulse flag when we think there is a pulse
              IBI = sampleCounter - lastBeatTime;       
              lastBeatTime = sampleCounter;               

              if secondBeat :                        # if this is the second beat, if secondBeat == TRUE
                secondBeat = False;                  # clear secondBeat flag
                for i in range(0,10):             # seed the running total to get a realisitic BPM at startup
                  rate[i] = IBI;                      

              if firstBeat :                        # if it's the first time we found a beat, if firstBeat == TRUE
                firstBeat = False;                   # clear firstBeat flag
                secondBeat = True;                   # set the second beat flag
                continue                          


              
              runningTotal = 0;                

              for i in range(0,9):                
                rate[i] = rate[i+1];                
                runningTotal += rate[i];              

              rate[9] = IBI;                          
              runningTotal += rate[9];                
              runningTotal /= 10;                   
              BPM = 60000/runningTotal;             
              streamer.log("Heart-Beat Rate",BPM)
              print ('BPM: {}'.format(BPM))

        if Signal < thresh and Pulse == True :   
            Pulse = False;                         
            amp = P - T;                          
            thresh = amp/2 + T;                    
            P = thresh;                          
            T = thresh;

        if N > 2500 :                         
            thresh = 512;                        
            P = 512;                              
            T = 512;                              
            lastBeatTime = sampleCounter;            
            firstBeat = True;                      
            secondBeat = False;                   
            print (z)

        time.sleep(0.005)
    
 streamer.close()
