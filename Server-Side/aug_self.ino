#include <Multichannel_Gas_GMXXX.h>

// if you use the software I2C to drive the sensor, you can uncomment the define SOFTWAREWIRE which in Multichannel_Gas_GMXXX.h.
#ifdef SOFTWAREWIRE
    #include <SoftwareWire.h>
    SoftwareWire myWire(3, 2);
    ++-
    GAS_GMXXX<SoftwareWire> gas;
#else
    #include <Wire.h>
    GAS_GMXXX<TwoWire> gas;
#endif

static uint8_t recv_cmd[8] = {};
const int analogInPin = A0;      // Analog input pin connected to the mux output
const int s0 = 2;            // Pin connected to S0 control pin of the mux
const int s1 = 3;            // Pin connected to S1 control pin of the mux
const int s2 = 4;            // Pin connected to S2 control pin of the mux
const int s3 = 5;   
void setup() {
  // put your setup code here, to run once:
  pinMode(s0,OUTPUT);
  pinMode(s1,OUTPUT);
  pinMode(s2,OUTPUT);
  pinMode(s3,OUTPUT);
  Serial.begin(9600);
  gas.begin(Wire, 0x08);

}
int mux[]={0,0,0,0,0,0,0,0,0,0,0};
void setMuxChannel(int channel)
{
    digitalWrite(s0,bitRead(channel,0));
    digitalWrite(s1,bitRead(channel,1));
    digitalWrite(s2,bitRead(channel,2));
    digitalWrite(s3,bitRead(channel,3));
}
void displayData()
// dumps captured data from array to serial monitor
{
   for (int i = 0; i < 11; i++) {
    Serial.print(mux[i]);
    if (i < 10) {
      Serial.print(",");
    }
  }
  Serial.println();  // Move to the next line after printing the values
}

void loop() {
//   Serial.println(mux[0]);
  // put your main code here, to run repeatedly:
  uint8_t len = 0;
    uint8_t addr = 0;
    uint8_t i;
    uint32_t val = 0;
  for(int i=0;i<11;i++)
  {
    setMuxChannel(i);
    if(i<7)
    {
    
         mux[i]=analogRead(analogInPin);
    }
    else if(i==7)
     {
      val = gas.getGM102B();
      mux[i]=round((gas.calcVol(val)*1024)/5);
     }
     else if(i==8)
     {
      val = gas.getGM302B();
      mux[i]=round((gas.calcVol(val)*1024)/5);
     }
     else if(i==9)
     {
      val = gas.getGM502B();
      mux[i]=round((gas.calcVol(val)*1024)/5);
     }
     else
     {
      val = gas.getGM702B();
      mux[i]=round((gas.calcVol(val)*1024)/5);
     }
   
    delay(10);
    
  }
  displayData();
//  for(int i=0;i<15;i++)
//  {
//    mux[i]=0;
//  }
  delay(500); 
  

}
