class Solution {
    public boolean isAnagram(String s, String t) {
	    if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> wordS = new HashMap<>();
        Map<Character, Integer> wordT = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            wordS.put(s.charAt(i), wordS.getOrDefault(s.charAt(i), 0) + 1);
            wordT.put(t.charAt(i), wordT.getOrDefault(t.charAt(i), 0) + 1);

        }
        return wordS.equals(wordT);

    }
}
