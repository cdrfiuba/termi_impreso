void setup() 
{ 
	Serial.begin(9600); //inicio conexion serie
}

int v[5]={1,2,3,4,5};
String string;
int p;

void loop() 
{   
  
  //loopear();
   crear_string();
   Serial.println(string);

}

void crear_string(){
    string = "<";
    for(p=0;p<4;p++){
    string.concat(v[p]);
    string.concat(",");
    }
    string.concat(v[4]);
    string.concat(">");
}
  
