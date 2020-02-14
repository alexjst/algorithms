class Contest162D {
    public static void main(String[] args) {
        
    }

    public int maxScoreWords(String[] words, char[] letters, int[] score) {
        int[] weights = new int[26];  // pool, weight for each char, changed if used
        for (char c : letters) {
            weights[c-'a']++;
        }
        int[] costs = new int[words.length]; // each word's cost, not changing
        for (int i=0; i<words.length; i++) {
            int[] wordWeights = new int[26];
            char[] wchars = words[i].toCharArray();
            for (char c : wchars) {
                costs[i] += score[c-'a'];
                wordWeights[c-'a']++;
                if (wordWeights[c-'a']>weights[c-'a']) {
                    costs[i] = -1;
                    break;
                }
            }
        }
        
        Integer res = 0;
        dfs(words, -1, weights, costs, 0, res);
        return res;
    }
    
    void dfs(String[] words, int start, int[] weights, int[] costs, int score, Integer maxScore) {
        maxScore = Math.max(maxScore, score);
        System.out.println("Max Score is now: " + maxScore);
        if ((start+1)>=words.length) return;
        
        // use the word at start+1, should have changed weights (pool), changed score, possiblely changed maxScore
        int[] nweights = new int[26];
        for (int i=0; i<26; i++) {
            nweights[i] = weights[i];
        }
        char[] wchars = words[start+1].toCharArray();
        boolean canChoose = true;
        System.out.println("start="+start);
        for (char c: wchars) {
            nweights[c-'a']--;
            if (nweights[c-'a']<0) {
                canChoose = false;
                break;
            }
        }
        if (canChoose) {
            System.out.println("Can choose " + (start+1) + " of cost " + costs[start+1]);
            dfs(words, start+1, nweights, costs, score+costs[start+1], maxScore);

        } else {
            System.out.println("Can NOT choose " + (start+1));
        }
        
        // skip the word at start+1
        dfs(words, start+2, weights, costs, score, maxScore);
    }
}