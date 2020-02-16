import java.io.*;
import java.util.*;

class Main{
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringBuilder sb = null;
    static StringTokenizer st = null;

    public static void main(final String[] args) throws IOException {
        int arrSize = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int[] result = new int[arrSize];
        int height=0;
        int leftNum=0;
        int cnt = 0;

        for (int i = 0; st.hasMoreTokens(); i++) {
            height = i+1;
            leftNum = Integer.parseInt(st.nextToken());
            
            for (int j = 0; j < result.length; j++) {
                if(cnt==leftNum && result[j]==0){
                    result[j]=height;
                    break;
                }
                if(result[j]>height || result[j] == 0){
                    cnt++;
                }
            }

            cnt = 0;
        }

    
        for (int i : result) {
            bw.write(String.valueOf(i));
            if(i!=result[result.length-1])bw.write(" ");
        }
        
        bw.flush();
    }
}
