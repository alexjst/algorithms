/**
 * This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
 */

 /**
  * This is the best solution on LC
  */
 import java.util.List;
 import java.util.ArrayList;

class Problem_20190901_Autocomplete {
    public static class TrieNode {
        public boolean isWord; 
        public TrieNode[] children = new TrieNode[26];
        public TrieNode() {}
    }
    public static class Trie {
        public add(String instr) {
            int len = instr.length();
            while (nodes.size()<(len+1)) nodes.add(new Node());

            for (int i=0; i<len; i++) {
                char c = instr.charAt(i);
                int idx = c - 'a';
                nodes[idx] = 1;
            }
        }
        public Trie() {
            List<Node> nodes = new ArrayList<>();
            nodes.add(new Node());
        }
    }

    public static Trie buildTrie(String[] dict) {
        if (dict==null || dict.length==0) return null;

    }

    public static void main(String[] args) {
        String[] dict = new String[] { "dog", "deer", "deal" };
        String[] result = getCompleteQueries(dict, "de");
        for (String r : result) {
            System.out.println(r);
        }
    }

    private static String[] getCompleteQueries(String[] dict, String prefix) {
        if (dict==null || dict.length==0) return dict;
    }
}

