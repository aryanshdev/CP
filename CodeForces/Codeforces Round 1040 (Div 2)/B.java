import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class B {

    static class State {
        int index;
        int sum;

        State(int index, int sum) {
            this.index = index;
            this.sum = sum;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            solve(br);
        }
    }

    private static void solve(BufferedReader br) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int c0 = 0, c1 = 0, c2 = 0;
        for (int i = 0; i < n; i++) {
            int val = Integer.parseInt(st.nextToken());
            if (val == 0) {
                c0++;
            } else if (val == 1) {
                c1++;
            } else {
                c2++;
            }
        }

        int[] b = new int[n];
        int ptr = 0;
        for (int i = 0; i < c0; i++) b[ptr++] = 0;
        for (int i = 0; i < c2; i++) b[ptr++] = 2;
        for (int i = 0; i < c1; i++) b[ptr++] = 1;

        boolean[][] visited = new boolean[n][s + 1];
        Queue<State> queue = new LinkedList<>();

        if (b[0] <= s) {
            queue.add(new State(0, b[0]));
            visited[0][b[0]] = true;
        }

        boolean found = false;
        while (!queue.isEmpty()) {
            State current = queue.poll();
            int u = current.index;
            int currentSum = current.sum;

            if (u == n - 1 && currentSum == s) {
                found = true;
                break;
            }

            if (u > 0) {
                int nextSum = currentSum + b[u - 1];
                if (nextSum <= s && !visited[u - 1][nextSum]) {
                    visited[u - 1][nextSum] = true;
                    queue.add(new State(u - 1, nextSum));
                }
            }
            if (u < n - 1) {
                int nextSum = currentSum + b[u + 1];
                if (nextSum <= s && !visited[u + 1][nextSum]) {
                    visited[u + 1][nextSum] = true;
                    queue.add(new State(u + 1, nextSum));
                }
            }
        }

        if (found) {
            System.out.println(-1);
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n; i++) {
                sb.append(b[i]).append(" ");
            }
            System.out.println(sb.toString().trim());
        }
    }
}