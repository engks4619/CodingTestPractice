package BaekJoon.입출력과사칙연산;
import java.util.Scanner;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class AplusB_1000 {
  // Scanner 사용
  // public static void main(String[] args) {
  //   Scanner in = new Scanner(System.in);
  //   int a = in.nextInt();
  //   int b = in.nextInt();
  //   System.out.println(a+b);
  //   in.close();
  // }
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] str = br.readLine().split(" ");
    int a = Integer.parseInt(str[0]);
    int b = Integer.parseInt(str[1]);
    System.out.println(a+b);
  }  
}
