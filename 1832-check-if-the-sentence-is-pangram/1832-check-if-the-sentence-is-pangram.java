class Solution {
    public boolean checkIfPangram(String sentence) {
        ArrayList<Character> list = new ArrayList<>();
        for(int i=0; i<sentence.length(); i++){
            char ch = sentence.charAt(i);
            if(!list.contains(ch)){
                list.add(ch);
            }
        }
        if(list.size() == 26){
            return true;
        }
        return false;
    }
}