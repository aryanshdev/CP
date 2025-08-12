import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;

public class submission {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());

            int[] counts = new int[52];
            long totalSum = 0;
            for (int i = 0; i < n; i++) {
                int num = Integer.parseInt(st.nextToken());
                if (num <= 50) {
                    counts[num]++;
                }
                totalSum += num;
            }

            long[][] dp = new long[53][n + 1];
            for (int i = 0; i < dp.length; i++) {
                Arrays.fill(dp[i], Long.MIN_VALUE / 2);
            }

            dp[0][n] = 0;

            for (int i = 1; i <= 52; i++) {
                for (int j = 0; j <= n; j++) {
                    if (dp[i-1][j] <= Long.MIN_VALUE / 4) {
                        continue;
                    }
                    for (int p = 0; p <= counts[i-1]; p++) {
                        int k = Math.min(j, p);
                        long val = dp[i-1][j] + (long) k - (long) (i - 1) * p;
                        dp[i][k] = Math.max(dp[i][k], val);
                    }
                }
            }

            long maxMexBenefit = 0;
            for (int k = 0; k <= n; k++) {
                maxMexBenefit = Math.max(maxMexBenefit, dp[52][k]);
            }

            System.out.println(totalSum + maxMexBenefit);
        }
    }
}