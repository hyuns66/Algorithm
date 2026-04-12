import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_12871 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String fs = br.readLine();
        String ft = br.readLine();

        // 각 문자열의 길이는 50보다 작거나 같은 자연수(알파벳 소문자로만 이루어짐)
        String s; // 더 작은 문자열
        String l; // 더 긴 문자열
        if(fs.length()<ft.length()){
            s = fs;
            l = ft;
        }else{
            s = ft;
            l = fs;
        }

        int answer = 0; // 같은 문자열을 만들면 1, 아니면 0
        if(l.length()%s.length()==0){ // 작은 문자열의 배수가 아니면 무조건 0이 답이므로.
            boolean isEqual = true;
            for(int i=0; i<l.length(); i++){
                if(l.charAt(i)!=s.charAt(i%s.length())){
                    isEqual = false;
                    break;
                }
            }

            if(isEqual) answer = 1;
        }

        System.out.print(answer);

    }
}
