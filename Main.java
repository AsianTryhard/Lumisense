import java.awt.*;
import javax.swing.*; 

class Main {
	public static void main(String[] args) {
		JFrame frame = new JFrame("Simple GUI");
	    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	    frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
	    frame.setUndecorated(true);

	    Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
		Point middle = new Point(screenSize.width / 2, screenSize.height / 2);
		Point newLocation = new Point(middle.x - (frame.getWidth() / 2), 
		                              middle.y - (frame.getHeight() / 2));
		frame.setLocation(newLocation);
		frame.setSize(500, 500);
		frame.setVisible(true); 
		frame.getContentPane().setBackground(Color.YELLOW);


	    JButton b1=new JButton("Upload hoto");  
	    b1.setBounds(50,100,120,50);  
	    frame.add(b1);
	    JButton b2=new JButton("Calibrate");  
	    b2.setBounds(350,100,120,50);  
	    frame.add(b2);
	    JButton b3=new JButton("Upload Photo"); 
	    b3.setBounds(50,200,120,50);  
	    frame.add(b3);
	    Rectangle b4=new Rectangle(50,300,120,50);
	    frame.add(b4);
	}
}