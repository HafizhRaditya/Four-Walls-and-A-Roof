public class message{
    String name;
    String message;
    String occupation;

public message(String name, String message, String occupation){
    this.name = name;
    this.message = message;
    this.occupation = occupation;
}
public void displayinfo(){
    System.out.println("==========");
    System.out.println("Name : " +name);
    System.out.println("Message : " +message);
    System.out.println("Occupation : " +occupation);
}

public static void main(String[] args) {
    message rust = new  message("Rustin Cohle", "All hands and hands walk into extinction", "State Detective");
    message tyler = new message("Tyler Durden", "You are the all singin all dancing crap in the world", "Soap Maker");
    message patrick = new message("Patrick Bateman", "This confession has meant nothing", "Banker");
    message lou = new message("Lou Bloom", "You have to get the money...to buy the ticket", "Stringer");
    message k = new message("Officer KD6-3.7", "Cells", "LAPD Officer");
    message rick = new message("Rick Grimes", "We are the ones who lives", "King County Sheriff");

    rust.displayinfo();
    tyler.displayinfo();
    patrick.displayinfo();
    lou.displayinfo();
    k.displayinfo();
    rick.displayinfo();
}
}