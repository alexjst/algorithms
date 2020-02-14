//package alexyang.algorithms.Java.Opendoor;

import java.io.*;
import java.util.*;

import java.io.*;
import java.util.*;

class Problem2 {
    Map<String, Set<ListNameRank>> map = new HashMap<>();

    HashMap<String, String[]> babyNames = new HashMap<>();
  

  public static void main(String[] args) {
    Problem2 p2 = new Problem2();
    p2.init();
    List<ListNameRank> list = p2.getBabyList("sophia");
    for (ListNameRank listNameRank : list) {
        System.out.println(listNameRank.listName + " : rank = " + listNameRank.rank);
    }
  }

  public static class ListNameRank {
      String listName;
      Integer rank;
      public ListNameRank(String name, int rank) {
          this.listName = name;
          this.rank = rank;
      }
      public boolean equals(Object o) {
          // If the object is compared with itself then return true   
        if (o == this) { 
            return true; 
        } 
  
        if (!(o instanceof ListNameRank)) { 
            return false; 
        } 
          
        ListNameRank c = (ListNameRank) o; 
          
        // Compare the data members and return accordingly  
        return this.listName.equals(c.listName) && this.rank == c.rank; 
        } 
    }


  public void init() {
    babyNames.put("2016-baby-center-girls",
        new String[] { "Sophia", "Emma", "Olivia", "Ava", "Mia", "Isabella", "Riley", "Aria", "Zoe", "Charlotte",
            "Lily", "Layla", "Amelia", "Emily", "Madelyn", "Aubrey", "Adalyn", "Madison", "Chloe", "Harper", "Abigail",
            "Aaliyah", "Avery", "Evelyn", "Kaylee", "Ella", "Ellie", "Scarlett", "Arianna", "Hailey", "Nora", "Addison",
            "Brooklyn", "Hannah", "Mila", "Leah", "Elizabeth", "Sarah", "Eliana", "Mackenzie", "Peyton", "Maria",
            "Grace", "Adeline", "Elena", "Anna", "Victoria", "Camilla", "Lillian", "Natalie" });
    babyNames.put("2016-baby-center-boys",
        new String[] { "Jackson", "Aiden", "Lucas", "Liam", "Noah", "Ethan", "Mason", "Caden", "Oliver", "Elijah",
            "Grayson", "Jacob", "Michael", "Benjamin", "Carter", "James", "Jayden", "Logan", "Alexander", "Caleb",
            "Ryan", "Luke", "Daniel", "Jack", "William", "Owen", "Gabriel", "Matthew", "Connor", "Jayce", "Isaac",
            "Sebastian", "Henry", "Muhammad", "Cameron", "Wyatt", "Dylan", "Nathan", "Nicholas", "Julian", "Eli",
            "Levi", "Isaiah", "Landon", "David", "Christian", "Andrew", "Brayden", "John", "Lincoln" });
    babyNames.put("2015-baby-center-girls",
        new String[] { "Sophia", "Emma", "Olivia", "Ava", "Mia", "Isabella", "Zoe", "Lily", "Emily", "Madison",
            "Amelia", "Riley", "Madelyn", "Charlotte", "Chloe", "Aubrey", "Aria", "Layla", "Avery", "Abigail", "Harper",
            "Kaylee", "Aaliyah", "Evelyn", "Adalyn", "Ella", "Arianna", "Hailey", "Ellie", "Nora", "Hannah", "Addison",
            "Mackenzie", "Brooklyn", "Scarlett", "Anna", "Mila", "Audrey", "Isabelle", "Elizabeth", "Leah", "Sarah",
            "Lillian", "Grace", "Natalie", "Kylie", "Lucy", "Makayla", "Maya", "Kaitlyn" });
    babyNames.put("2015-baby-center-boys",
        new String[] { "Jackson", "Aiden", "Liam", "Lucas", "Noah", "Mason", "Ethan", "Caden", "Logan", "Jacob",
            "Jayden", "Oliver", "Elijah", "Alexander", "Michael", "Carter", "James", "Caleb", "Benjamin", "Jack",
            "Luke", "Grayson", "William", "Ryan", "Connor", "Daniel", "Gabriel", "Owen", "Henry", "Matthew", "Isaac",
            "Wyatt", "Jayce", "Cameron", "Landon", "Nicholas", "Dylan", "Nathan", "Muhammad", "Sebastian", "Eli",
            "David", "Brayden", "Andrew", "Joshua", "Samuel", "Hunter", "Anthony", "Julian", "Dominic" });
    babyNames.put("2015-us-official-girls", new String[] { "Emma", "Olivia", "Sophia", "Ava", "Isabella", "Mia",
        "Abigail", "Emily", "Charlotte", "Harper" });
    babyNames.put("2015-us-official-boys", new String[] { "Noah", "Liam", "Mason", "Jacob", "William", "Ethan", "James",
        "Alexander", "Michael", "Benjamin" });


    for (Map.Entry<String,String[]> entry : babyNames.entrySet()) {
        String listName = entry.getKey();
        String[] names = entry.getValue();
        int rank = 1;
        for (String name : names) {
            name = name.toLowerCase();
            ListNameRank listNameRank = new ListNameRank(listName, rank);
            if (map.containsKey(name)) {
                Set<ListNameRank> set = map.get(name);
                set.add(listNameRank);
            } else {
                Set<ListNameRank> set = new TreeSet<>(new Comparator<ListNameRank>(){
                    public int compare(ListNameRank o1, ListNameRank o2) {
                        if (o1.rank != o2.rank) {
                            return o1.rank - o2.rank;
                        } else {
                            return o1.listName.compareTo(o2.listName);
                        }
                    }
              });
              set.add(listNameRank);
              map.put(name, set);
            }
            rank++;
        }
    }
  }

  List<ListNameRank> getBabyList(String name) {
      name = name.toLowerCase();
      List<ListNameRank> res = new ArrayList<>();
      if (!map.containsKey(name)) {
        return res;
      }

    return new ArrayList<ListNameRank>(map.get(name));
  }
}