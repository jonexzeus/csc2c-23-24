public class While {
    public static void main(String[] args) {
        int sum=0;
        
        int i=0;

        do{
            
            i++;
            System.out.println(i);
            sum=sum+i;
           
        }while(i<=10);
        
        System.out.println("the sum is:"+sum);
    }
}
