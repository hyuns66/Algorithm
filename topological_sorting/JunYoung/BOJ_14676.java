import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

/**
 * 영우는 사기꾼?
 * - 우주 전쟁에서는 건물을 짓는 순서가 정해져있다.
 * - 치트키를 쓰면 원하는 건물을 마음대로 건설할 수 있다.
 * - 영선이와 영우는 서로 치트키를 쓰지 않기로 했다.
 * - 이상하게도 영우는 영선이와의 게임에서 모두 승리하였다. -> 치트키 사용의심
 * - 영우의 건설/파괴정보를 가져와서 영우가 치트키를 사용했는지 판단해보자
 *
 *  정렬은 아니고, inOrder를 이용해서 건물을 세울 수 있는지 없는지를 보는 것이었다.
 *  건물의 중복 건설이 가능했기에 건물이 생겼을 때만, inOrder를 증가시키고, 건물이 아예 없어졌을 때만 inOrder를 감소시키는 로직이 필요했다.
 *
 *  시간복잡도 해소) 매번 건설을 할 때마다, 이전 건물들의 건설 여부를 탐색하면 시간초과
 *                inOrder를 통해 현재 건물의 건설가능 여부를 바로 파악하고, 다음 건물들의 inOrder를 조작해서 다음 건물들의 건설여부를 업데이트 해준다.
 */
public class BOJ_14676 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int buildingNum = Integer.parseInt(st.nextToken());
        int edgeNum = Integer.parseInt(st.nextToken());
        int infoNum = Integer.parseInt(st.nextToken());

        ArrayList<Integer>[] graph = new ArrayList[buildingNum+1];
        for(int i=1; i<=buildingNum; i++){
            graph[i] = new ArrayList<>();
        }

        int[] inOrder = new int[buildingNum+1];
        for(int i=0; i<edgeNum; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            graph[x].add(y);
            inOrder[y] += 1;
        }

        int[] isBuild = new int[buildingNum+1];
        boolean isLier = false;
        for(int i=0; i<infoNum; i++){
            st = new StringTokenizer(br.readLine());
            int command = Integer.parseInt(st.nextToken());
            int bn = Integer.parseInt(st.nextToken());

            if(command==1){ // 건설이면
                boolean canBuild = inOrder[bn] == 0;

                if(canBuild){
                    isBuild[bn] += 1;
                    for(int next: graph[bn]){
                        if(isBuild[bn]==1){ // 첫번째 건물에 대해서만
                            inOrder[next] -= 1;
                        }
                    }
                }else{
                    // 건설할 수 없는 건물을 건설했다면
                    isLier = true;
                    break;
                }
                continue;
            }

            if(command==2){ // 파괴의 경우
                if(isBuild[bn]==0){
                    // 건설된 적 없는 건물이 파괴되었다면
                    isLier = true;
                    break;
                }

                isBuild[bn] -= 1;
                for(int next: graph[bn]){
                    if (isBuild[bn]==0){ // 아예 건물이 없어진 경우에만
                        inOrder[next] += 1;
                    }
                }
            }
        }

        if(isLier){
            System.out.println("Lier!");
        }else{
            System.out.println("King-God-Emperor");
        }
    }
}
