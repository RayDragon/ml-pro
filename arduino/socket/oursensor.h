#include <Wire.h>
class OurSensor{public:
  
// Faltu ka copy paste unknown constant decelerations
                // MPU6050 Slave Device Address

                const uint8_t MPU6050SlaveAddress = 0x68;

        // Select SDA and SCL pins for I2C communication 
        
                const uint8_t scl = D5;
                const uint8_t sda = D6;
      
        // sensitivity scale factor respective to full scale setting provided in datasheet 
                const uint16_t AccelScaleFactor = 16384;
                const uint16_t GyroScaleFactor = 131;

        // MPU6050 few configuration register addresses
                const uint8_t MPU6050_REGISTER_SMPLRT_DIV   =  0x19;
                const uint8_t MPU6050_REGISTER_USER_CTRL    =  0x6A;
                const uint8_t MPU6050_REGISTER_PWR_MGMT_1   =  0x6B;
                const uint8_t MPU6050_REGISTER_PWR_MGMT_2   =  0x6C;
                const uint8_t MPU6050_REGISTER_CONFIG       =  0x1A;
                const uint8_t MPU6050_REGISTER_GYRO_CONFIG  =  0x1B;
                const uint8_t MPU6050_REGISTER_ACCEL_CONFIG =  0x1C;
                const uint8_t MPU6050_REGISTER_FIFO_EN      =  0x23;
                const uint8_t MPU6050_REGISTER_INT_ENABLE   =  0x38;
                const uint8_t MPU6050_REGISTER_ACCEL_XOUT_H =  0x3B;
                const uint8_t MPU6050_REGISTER_SIGNAL_PATH_RESET  = 0x68;

                
                // Jo samajh aate hai wo wale variables
                int16_t AccelX, AccelY, AccelZ, Temperature, GyroX, GyroY, GyroZ;
                
                
      
                // constructor faltu ka
                OurSensor(){
                  //ghanta nai krna maine kuch yahan
                  
                }
                void I2C_Write(uint8_t deviceAddress, uint8_t regAddress, uint8_t data){
                   Wire.beginTransmission(deviceAddress);
                    Wire.write(regAddress);
                    Wire.write(data);
                    Wire.endTransmission();
                 }
                
                void init(){
                  // Bole to sensor initialize krne ka
                  Wire.begin(sda, scl);
                  delay(150);
                    I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_SMPLRT_DIV, 0x07);
                    I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_PWR_MGMT_1, 0x01);
                    I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_PWR_MGMT_2, 0x00);
                    I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_CONFIG, 0x00);
                    I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_GYRO_CONFIG, 0x00);//set +/-250 degree/second full scale
                    I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_ACCEL_CONFIG, 0x00);// set +/- 2g full scale
                    I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_FIFO_EN, 0x00);
                    I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_INT_ENABLE, 0x01);
                    I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_SIGNAL_PATH_RESET, 0x00);
                    I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_USER_CTRL, 0x00);
                }
                
                
                void updateValues(){
                  // Yahan apna sensor kai baar dimag gawa deta hai, so just in case galt value aa ri ho to bolne ka ki dubaara initialize ho ja
                  Read_RawValue(MPU6050SlaveAddress, MPU6050_REGISTER_ACCEL_XOUT_H);
                  /*if( 
                    Ax == Ay && 
                    Ay == Az && 
                    Az==-0.00 &&
                    T == 36.0 &&
                    Gx == -1
                
                    
                    ){
                    // kuch to gadbad hai
                    init();
                  }*/
                }
                void Read_RawValue(uint8_t deviceAddress, uint8_t regAddress){
                  Wire.beginTransmission(deviceAddress);
                  Wire.write(regAddress);
                  Wire.endTransmission();
                  Wire.requestFrom(deviceAddress, (uint8_t)14);
                  AccelX = (((int16_t)Wire.read()<<8) | Wire.read());
                  AccelY = (((int16_t)Wire.read()<<8) | Wire.read());
                  AccelZ = (((int16_t)Wire.read()<<8) | Wire.read());
                  Temperature = (((int16_t)Wire.read()<<8) | Wire.read());
                  GyroX = (((int16_t)Wire.read()<<8) | Wire.read());
                  GyroY = (((int16_t)Wire.read()<<8) | Wire.read());
                  GyroZ = (((int16_t)Wire.read()<<8) | Wire.read());

                }
                
                double Ax, Ay, Az, T, Gx, Gy, Gz;
                
                double get_ax(){Ax = (double)AccelX/AccelScaleFactor;return Ax;}
                double get_ay(){Ay = (double)AccelY/AccelScaleFactor;return Ay;}
                double get_az(){Az = (double)AccelZ/AccelScaleFactor;return Az;}
                double get_t(){T = (double)Temperature/340+36.53; return T;}
                double get_gx(){Gx = (double)GyroX/GyroScaleFactor;}
                double get_gy(){Gy = (double)GyroY/GyroScaleFactor;}
                double get_gz(){Gz = (double)GyroZ/GyroScaleFactor;}
                
};
