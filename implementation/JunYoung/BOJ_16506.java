import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * CPU
 * 민호가 직접 설계한 16-bit CPU 명령어 구조를 보고, (https://www.acmicpc.net/problem/16506)
 * 어셈블리어 코드가 주어졌을 때, 이를 기계어 코드로 번역하는 어셈블러를 만들어보자.
 */
public class BOJ_16506 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int commandNum = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for(int i=0; i<commandNum; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            int result = Integer.parseInt(st.nextToken()); // 결과값을 저장할 레지스터의 번호(1~7)
            int a = Integer.parseInt(st.nextToken()); // 연산에 사용되는 레지스터의 번호(1~7)
            int b = Integer.parseInt(st.nextToken()); // 레지스터 B 또는, 상수 #C

            // 0~4 : CPU가 수행해야 할 연산을 나타내는 opcode이다. 만약 4번 bit가 0일 경우 레지스터 rB를, 1일 경우 상수 #C를 사용한다.
            int[] machineLanguage = new int[16];

            // 상수로 쓰는 지 여부
            if(command.charAt(command.length()-1)=='C'){
                machineLanguage[4] = 1;
                command = command.substring(0, command.length()-1);
            }else{
                machineLanguage[4] = 0;
            }

            switch (command){
                case "ADD":
                    machineLanguage[0] = 0;
                    machineLanguage[1] = 0;
                    machineLanguage[2] = 0;
                    machineLanguage[3] = 0;
                    break;
                case "SUB":
                    machineLanguage[0] = 0;
                    machineLanguage[1] = 0;
                    machineLanguage[2] = 0;
                    machineLanguage[3] = 1;
                    break;
                case "MOV":
                    machineLanguage[0] = 0;
                    machineLanguage[1] = 0;
                    machineLanguage[2] = 1;
                    machineLanguage[3] = 0;
                    break;
                case "AND":
                    machineLanguage[0] = 0;
                    machineLanguage[1] = 0;
                    machineLanguage[2] = 1;
                    machineLanguage[3] = 1;
                    break;
                case "OR":
                    machineLanguage[0] = 0;
                    machineLanguage[1] = 1;
                    machineLanguage[2] = 0;
                    machineLanguage[3] = 0;
                    break;
                case "NOT":
                    machineLanguage[0] = 0;
                    machineLanguage[1] = 1;
                    machineLanguage[2] = 0;
                    machineLanguage[3] = 1;
                    break;
                case "MULT":
                    machineLanguage[0] = 0;
                    machineLanguage[1] = 1;
                    machineLanguage[2] = 1;
                    machineLanguage[3] = 0;
                    break;
                case "LSFTL":
                    machineLanguage[0] = 0;
                    machineLanguage[1] = 1;
                    machineLanguage[2] = 1;
                    machineLanguage[3] = 1;
                    break;
                case "LSFTR":
                    machineLanguage[0] = 1;
                    machineLanguage[1] = 0;
                    machineLanguage[2] = 0;
                    machineLanguage[3] = 0;
                    break;
                case "ASFTR":
                    machineLanguage[0] = 1;
                    machineLanguage[1] = 0;
                    machineLanguage[2] = 0;
                    machineLanguage[3] = 1;
                    break;
                case "RL":
                    machineLanguage[0] = 1;
                    machineLanguage[1] = 0;
                    machineLanguage[2] = 1;
                    machineLanguage[3] = 0;
                    break;
                case "RR":
                    machineLanguage[0] = 1;
                    machineLanguage[1] = 0;
                    machineLanguage[2] = 1;
                    machineLanguage[3] = 1;
                    break;
            }

            // 5 : 사용하지 않는 bit이며, 항상 0이다.
            // 6~8 : 결괏값을 저장하는 레지스터 rD의 번호이다.
            String resultString = Integer.toBinaryString(result);
            //System.out.println("resultString = "+resultString);
            for(int j=0; j<resultString.length(); j++){
                machineLanguage[8-j] = resultString.charAt(resultString.length()-1-j)-'0';
            }

            // 9~11 : 연산에 사용되는 레지스터 rA의 번호이다. 사용하지 않을 경우에는 000이다.
            String aString = Integer.toBinaryString(a);
            //System.out.println("aString = "+aString);
            for(int j=0; j<aString.length(); j++){
                machineLanguage[11-j] = aString.charAt(aString.length()-1-j)-'0';
            }

            // 12~15 : 만약 4번 bit가 0일 경우 12~14번 bit는 연산에 사용되는 레지스터 rB의 번호이며, 15번 bit는 항상 0이다. 만약 4번 bit가 1일 경우 12~15번 bit는 상수 #C이다.
            String bString = Integer.toBinaryString(b);
            //System.out.println("bString = "+bString);
            if(machineLanguage[4]==0){
                for(int j=0; j<bString.length(); j++){
                    machineLanguage[14-j] = bString.charAt(bString.length()-1-j)-'0';
                }
            }else{
                for(int j=0; j<bString.length(); j++){
                    machineLanguage[15-j] = bString.charAt(bString.length()-1-j)-'0';
                }
            }

            for (int k : machineLanguage) {
                sb.append(k);
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
