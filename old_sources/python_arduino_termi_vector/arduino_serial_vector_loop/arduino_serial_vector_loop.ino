#include <Servo.h> 
#include <String.h>
#include <Stream.h>

//instancio los objetos Servo
Servo PWM_servo_1;
Servo PWM_servo_2;
Servo PWM_servo_3;
Servo PWM_servo_4;
Servo PWM_servo_5;
Servo PWM_servo_6;
Servo PWM_servo_7;
Servo PWM_servo_8;

//conexiones de los servos
const int AD_servo_1 = A5; //revisar, este es el que no funciona 
const int AD_servo_2 = A0;
const int AD_servo_3 = A1;
const int AD_servo_4 = A2;
const int AD_servo_5 = A3;
const int AD_servo_6 = A4;

int ad_vector[6]={0,0,0,0,0,0}; //este vector contiene las lecturas de los ADs
int ad_vector_e[12]={200,0,201,0,202,0,203,0,204,0,205,0}; //este vector contiene las lecturas de los ADs ya indexadas que luego se envia por serie
int pwm_vector[8]={0,0,0,0,0,0,0,0}; //este vector contiene la posicion a escribir en los servos.
int i,j,p,q,valor;
char input[16];

void setup() 
{ 
	Serial.begin(9600); //inicio conexion serie
	PWM_servo_1.attach(8);  //revisar esta conexion
        PWM_servo_2.attach(9);
        PWM_servo_3.attach(7);
        PWM_servo_4.attach(10);
        PWM_servo_5.attach(6);
        PWM_servo_6.attach(12);
        PWM_servo_7.attach(5);
        PWM_servo_8.attach(13);
} 

void loop() 
{   
  recibir_pwm_vector();			        //lee los angulos deseados enviadas desde pyhon y las almacena en vector pwm_vector
  //escribir_pwm_vector_a_servo();	//escribe el vector posc en los objetos servo.
  leer_AD();				        //actualiza vector AD_lecturas
  //loopear();
  indexar_ad_vector();
  enviar_ad_vector_e();
  
}

void loopear(){
  if(Serial.available()){
    for (q=0;q<8;q++){
      Serial.write(pwm_vector[q]);
      }
  }
}

void recibir_pwm_vector(){
     if(Serial.available()){
        int valor=Serial.read();
        if(valor==200){                 //esperamos a recibir el entero 200 para saber que lo que sigue es el 1er angulo
            //while (!Serial.available());
            pwm_vector[0] = Serial.read();
        }
        else if(valor==201){            //esperamos a recibir el entero 201 para saber que lo que sigue es el 2do angulo
            //while (!Serial.available());
            pwm_vector[1] = Serial.read();
        }            
        else if(valor==202){            
            //while (!Serial.available());
            pwm_vector[2] = Serial.read();
        }
        else if(valor==203){           
            //while (!Serial.available());
            pwm_vector[3] = Serial.read();
        }
        else if(valor==204){           // .... 
            //while (!Serial.available());
            pwm_vector[4] = Serial.read();
        }
        else if(valor==205){           
            //while (!Serial.available());
            pwm_vector[5] = Serial.read();
        }
        else if(valor==206){            
            //while (!Serial.available());
            pwm_vector[6] = Serial.read();
        }
        else if(valor==207){           
            //while (!Serial.available());
            pwm_vector[7] = Serial.read();
        }
}
}

void indexar_ad_vector(){
 ad_vector_e[1]=ad_vector[0];
 ad_vector_e[3]=ad_vector[1];
 ad_vector_e[5]=ad_vector[2];
 ad_vector_e[7]=ad_vector[3];
 ad_vector_e[9]=ad_vector[4];
 ad_vector_e[11]=ad_vector[5];
}


void escribir_pwm_vector_a_servo(){
 PWM_servo_1.write(pwm_vector[0]);
 PWM_servo_2.write(pwm_vector[1]); 
 PWM_servo_3.write(pwm_vector[2]);  
 PWM_servo_4.write(pwm_vector[3]); 
 PWM_servo_5.write(pwm_vector[4]);
 PWM_servo_6.write(pwm_vector[5]);
 PWM_servo_7.write(pwm_vector[6]);
 PWM_servo_8.write(pwm_vector[7]); 
}

void leer_AD(){
  ad_vector[0] = 1; //analogRead(AD_servo_1);
  ad_vector[1] = analogRead(AD_servo_2);
  ad_vector[2] = analogRead(AD_servo_3);
  ad_vector[3] = analogRead(AD_servo_4);
  ad_vector[4] = analogRead(AD_servo_5);
  ad_vector[5] = analogRead(AD_servo_6);
}


void enviar_ad_vector_e(){
  if(Serial.available()){
    for (q=0;q<12;q++){
      while (!Serial.available());
      Serial.write(ad_vector_e[q]);
      }
  }
}

