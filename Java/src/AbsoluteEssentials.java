/**
 * This class contains demos code that are absolute Java essentails that are
 * needed to write algorithmic solutions quickly.
 * 
 */

 import java.util.*;

class AbsoluteEssentials {
    public static void main(String[] args) {
        /**
         * 1. how to sort an object by its property.
         * 2. how to use priority queue.
         * 3. how to convert from numbers to string, and back.
         * 4. how to intialize arrays and List<>
         * 5. how to copy 2D array
         * 6. how to do binary search
         * 7. how to implement C++'s lower_bound and upper_bound
         * 8. how to use Stack and Queue
         * 9. BFS template with Queue
         * 10. How to iterate through a Set and a Map
         * 11. How to do random shuffle and generate a random integer number within a range.
         */

        /* 1. How to sort an object by its property? Let's say, let's compare
              strings be length and we want to sort in descending order, meaning
              we want to rank the longest string first, the shortest string last.
        */
        // Use Arrays for array
        String[] myStrings = {"hello", "how", "are", "you", "doing"};
        printStringList("Original", myStrings);
        Arrays.sort(myStrings);
        printStringList("Arrays.sort", myStrings);
        Arrays.sort(myStrings, Collections.reverseOrder());
        printStringList("Arrays.sort reverse order", myStrings);
        Arrays.sort(myStrings, new Comparator<String>() {public int compare(String a, String b) { return a.length() - b.length(); }});
        printStringList("Arrays.sort by length", myStrings);
        Arrays.sort(myStrings, new Comparator<String>() {public int compare(String a, String b) { return b.length() - a.length(); }});
        printStringList("Arrays.sort by length in reverse order", myStrings);

        // Use Collections for List
        List<String> myStrs = Arrays.asList("hello", "how", "are", "you", "doing");
        printStringList("Original", myStrs);
        Collections.sort(myStrs);
        printStringList("Collections order", myStrs);
        Collections.sort(myStrs, Collections.reverseOrder());
        printStringList("Collections reverse order", myStrs);
        Collections.sort(myStrs, new Comparator<String>() {
            public int compare(String a, String b) {
                return a.length() - b.length();
            }
        });
        printStringList("Collections sort by length", myStrs);
        Collections.sort(myStrs, new Comparator<String> () {
            public int compare(String a, String b) {
                return b.length()- a.length();
            }
        });
        printStringList("Collections sort by length reverse order", myStrs);
        System.out.println();

        /**
         * 2. Using a priority queue. The following example demonstrate using a priority
         * queue to always show the second largest item in a stream of integers, meaning
         * we need a minHeap.
         * 
         * It is interesting that Java PriorityQueue is a min heap by default, while C++
         * priority_queue is a max heap by default.
         */
        int[] streams = {4,7,17,82,5,7,8,18,9,22,8,6,4,44,99,4,5,6,7,8,6,35,55,5,455,14,4,54,47,234,354,5,46,4,6,46,4};
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int num : streams) {
            pq.offer(num);
            if (pq.size()==3) {
                pq.poll();
            }
            if (pq.size()==2) {
                System.out.print(pq.peek() + "\t");
            }
        }
        System.out.println();

        /**
         * 3. How to convert from String to number and back.
         * 
         * From String to number: use NumberType.parseNumberType
         * From number to String: String.valueOf();
         */
        System.out.println(Integer.parseInt("123"));
        System.out.println(Double.parseDouble("1.23"));
        System.out.println(String.valueOf("45.6"));

        /**
         * 4. How to initialize [] and List.
         * 
         * For array, just "= {1, 2, 3}". For List, use Arrays.asList(1,2,3);
         * 
         * We may sometimes want to use Arrays.fill(array, from, to, value) to set
         * initial values
         */
        int[] myArraySample = {1, 2, 3, 4};
        Arrays.fill(myArraySample, 2,3, 0);
        List<Integer> myListSample = Arrays.asList(1,2,3,4);
        Collections.fill(myListSample, 0);
        for (int n: myArraySample) System.out.println("Hello: " + n);

        /**
         * 5. How to copy 2D array.
         * Safest: copy one element by elment.
         */
        int[][] my2Darray = {{10,20}, {21,30}, {31,40}};
        Integer[][] my2DarrayCopy = new Integer[3][2];
        for (int i=0; i<3; i++) for (int j=0; j<2; j++) my2DarrayCopy[i][j] = my2Darray[i][j];
        // The following shows that clone() does not work. It's very shallow copy of references.
        Integer[][] anotherCopy = my2DarrayCopy.clone();
        for (int i=0; i<3; i++) for (int j=0; j<2; j++) anotherCopy[i][j] = 0;
        for (int i=0; i<3; i++) {
            for (int j=0; j<2; j++) {
                System.out.print(my2DarrayCopy[i][j] + " ");
            }
            System.out.println();
        }

        /**
         * 6. how to do binary search
         * Arrays.binarySearch(array, from, to, key, Comparator)
         */
        int[] myArraySampleSorted = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        System.out.println(Arrays.binarySearch(myArraySampleSorted, 10));

        /**
         * 7. How to implement lower_bound and upper_bound
         * 
         * There's actually no better way other than to implement it myself.
         * Or use Arrays/Collections binarySearch and reach out for equal range.
         */

        /**
         * 8. How to use Stack and Queue
         * 
         * Note that Queue is Interfaces, and the implemention can be LinkedList.
         * 
         * Stack.push(E). Stack.pop(). Stack.peek() Queue.offer(E), Queue.poll(),
         * Queue.peek() Deque.offerFirst(E), Deque.offerLast(E), Deque.pollFirst(E),
         * Deque.pollLast(E), Deque,peekFirst(), Deque.peekLast()
         */

         /**
          * 9. BFS Template
          */
        Queue<Integer> q = new LinkedList<>();
        q.offer(1); // first element
        while (!q.isEmpty()) {
            Integer e = q.peek();
            q.poll();
            if (e < 10) {
                e++;
                q.offer(e);
            }
        }

        /**
         * 10. How to iterate a map?
         */
        // set is simpler, with just one element in each set entry
        Set<Integer> mySet = new HashSet<>();
        mySet.add(1);
        for (Integer k: mySet) { System.out.println(k); }
        // for map, ther are 3 ways to iterate: key, values or entry as a whole
        Map<Integer, Integer> myMap = new HashMap<>();
        myMap.put(1,2);
        for (Integer k : myMap.keySet()) {
            System.out.println(k);
        }
        for (Integer v : myMap.values()) {
            System.out.println(v);
        }
        for (Map.Entry<Integer,Integer> entry : myMap.entrySet()) {
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }

        /**
         * 11. How to do random shuffle and random integer generation within a range?
         */
        // Random shuffle a List with Collections.
        List<Integer> shufTargetList = new ArrayList<>();
        Collections.shuffle(shufTargetList);
        // How to random shuttfle an array then? (not a list)
        int[] shufTargetArray = new int[]{1,2,3,4,5,6,7,8,9};
        Collections.shuffle(Arrays.asList(shufTargetArray));
        // Generate integer random numbrer within a range
        // Math.random() will get a random double from[0,1), that is including 0.9 but excluding 1.0
        // so Math.random() * N casted to an integer will be an integer between 0 and N-1.
        // for target range minInt and maxInt, N-1+minInt=maxInt so N = maxInt-minInt+1
        int minInt = 20, maxInt = 40;
        System.out.println( Math.random() * (maxInt - minInt + 1) + minInt); 


        return;
    }

    public static void printStringList(String prefix, List<String> in) {
        System.out.print(prefix + ": ");
        for (String s : in) {
            System.out.print(s + " ");
        }
        System.out.println();
    }
    public static void printStringList(String prefix, String[] in) {
        System.out.print(prefix + ": ");
        for (String s : in) {
            System.out.print(s + " ");
        }
        System.out.println();
    }
}