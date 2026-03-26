import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 민서의 응급 수술
 *
 * 뇌 속의 뉴런 = 하나의 트리 형태라고 생각해보자
 * 트리 = 사이클이 존재하지 않는 연결 그래프
 *
 * 모든 뉴런을 하나의 트리 형태로 연결하기 위한 최소 연산 횟수?
 *
 * ====================================
 *  다른 그룹이 몇 그룹인지 찾아내면 될 것 같은데
 *  union-find.. 그 그룹인지 아닌지를 체크하는 용으로는
 *  문제에서 a-b를 연결해라고 해도 그렇게 안하고 루트끼리 연결해버리면 상관없다!!
 *
 *  [분리집합~union-find]
 *  [트리+union-find]
 */
public class BOJ_20955 {
    static int[] parents; // 여기선 실제 부모-자식관계가 아니라, 이 그룹의 대표자를 나타내기 위한 거다.

    static int find(int a){
        if (a==parents[a]) return a; // 루트노드를 찾았으면 return;
        return find(parents[a]);
    }

    static boolean union(int a, int b){
        int pa = find(a);
        int pb = find(b);
        if(pa == pb){ // 부모가 같으면 union 불가
            return false;
        }
        //부모가 작은 값이 부모가 되도록
        if(pb < pa){
            parents[pa] = pb;
        }else{
            parents[pb] = pa;
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()); // 100000(십만)
        int neuron  = Integer.parseInt(st.nextToken()); // 100000(십만)
        int synapse  = Integer.parseInt(st.nextToken()); // 1~Math.min(N(N-1)/2, 100000(십만))

        // 각 뉴런의 부모 노드 저장
        parents = new int[neuron+1];
        for(int i=1; i<=neuron; i++){
            parents[i] = i; // 자기 자신을 부모로 설정해두기
        }

        // 시냅스 정보 입력 받기
        int breakCnt = 0;
        for(int i=0; i<synapse; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if(!union(a,b)) breakCnt++;
        }
//        System.out.println(breakCnt);
        //System.out.println(Arrays.toString(parents));

        int connectCnt = -1;
        for(int i=1; i<=neuron; i++){
            if (i==parents[i]) connectCnt++; // 부모노드의 수 세기
        }
        System.out.println(connectCnt+breakCnt);
    }
}
