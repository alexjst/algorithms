public class NumberToWords{
    private static List<String> numNames19 = 
        Arrays.asList("Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve",
                                         "Thirteen","Forteen","Fifteen","Sixteen","SevenTeen","Eighteen","Nineteen");
    private static List<Integer> nums99 =
        Arrays.asList(90, 80, 70, 60, 50, 40, 30, 20);
    private static List<String> numNames99 =
        Arrays.asList("Ninety", "Eighty", "Seventy", "Sixty", "Fifty", "Forty", "Thirty", "Twenty");
    
    private static List<Integer> numsBig =
        Arrays.asList(1000000000, 1000000, 1000, 100);
    private static List<String> namesBig =
        Arrays.asList("Billion", "Million", "Thousand", "Hundred");
    
    private StringBuilder result = new StringBuilder();
    
    public String numberToWords(int num) {
        if (num<=19) return numNames19.get(num);
        else if (num<=99) {
            for (int i=0; i<nums99.size(); i++) {
                int part = num / nums99.get(i);
                num = num % nums99.get(i);
                if (part > 0) {
                    result.append(" " + numNames99.get(i));
                    if (num > 0) result.append(" " + numberToWords(num));
                }
            }
        } else {        
            for (int i=0; i<numsBig.size(); i++) {
                int part = num / numsBig.get(i);
                num = num % numsBig.get(i);
                if (part > 0) {
                    result.append(" " + numberToWords(part));
                    result.append(" " + namesBig.get(i));
                    System.out.println("num = " + num + " part = " + part);
                }
            }
            if (num > 0) {
                result.append(" " + numberToWords(num));
            }
        }
        System.out.println(result.toString().trim());
        return result.toString().trim();
    }
    
    public static void main(String[] args) {
        NumberToWords s = new NumberToWords();
        s.numberToWords(123);
    }
}