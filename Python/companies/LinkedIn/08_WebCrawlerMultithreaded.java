/**
 * Problem 8: Web Crawler Multithreaded (Medium)
 *
 * **Java Concurrency Pattern - Thread Pools and Synchronization**
 *
 * Given a URL startUrl and an interface HtmlParser, implement a Multi-threaded web crawler
 * to crawl all links that are under the same hostname as startUrl.
 *
 * Return all URLs obtained by your web crawler in any order.
 *
 * Your crawler should:
 * - Start from the page: startUrl
 * - Call HtmlParser.getUrls(url) to get all URLs from a webpage
 * - Do not crawl the same link twice
 * - Explore only the links that are under the same hostname as startUrl
 * - Use multiple threads to speed up crawling
 *
 * Interface:
 *     interface HtmlParser {
 *         public List<String> getUrls(String url);
 *     }
 *
 * Example:
 * Input:
 * urls = [
 *   "http://news.yahoo.com",
 *   "http://news.yahoo.com/news",
 *   "http://news.yahoo.com/news/topics/",
 *   "http://news.google.com",
 *   "http://news.yahoo.com/us"
 * ]
 * edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
 * startUrl = "http://news.yahoo.com/news/topics/"
 *
 * Output: [
 *   "http://news.yahoo.com",
 *   "http://news.yahoo.com/news",
 *   "http://news.yahoo.com/news/topics/",
 *   "http://news.yahoo.com/us"
 * ]
 *
 * Explanation:
 * - Start from "http://news.yahoo.com/news/topics/"
 * - Crawl all URLs under "news.yahoo.com" hostname
 * - Do not crawl "http://news.google.com" (different hostname)
 *
 * Constraints:
 * - 1 <= urls.length <= 1000
 * - 1 <= urls[i].length <= 300
 * - startUrl is one of the urls
 * - Hostname label must be from 1 to 63 characters long
 * - All URLs are valid
 *
 * Approach:
 * - Use ConcurrentHashMap to track visited URLs (thread-safe)
 * - Use ExecutorService with thread pool for parallel crawling
 * - Use synchronization to avoid duplicate work
 * - Extract hostname from URL for comparison
 *
 * Key Concepts:
 * - ExecutorService and thread pools
 * - ConcurrentHashMap for thread-safe set operations
 * - CountDownLatch or phaser for tracking active tasks
 * - URL parsing and hostname extraction
 *
 * Time Complexity: O(N) where N is total URLs (with parallelism speedup)
 * Space Complexity: O(N) for visited set
 */

import java.util.*;
import java.util.concurrent.*;

interface HtmlParser {
    public List<String> getUrls(String url);
}

class WebCrawler {

    public List<String> crawl(String startUrl, HtmlParser htmlParser) {
        // TODO: Implement multi-threaded web crawler

        // Hints:
        // 1. Extract hostname from startUrl for comparison
        // 2. Use ConcurrentHashMap.newKeySet() for thread-safe visited set
        // 3. Create ExecutorService with fixed thread pool
        // 4. Use AtomicInteger to track pending tasks
        // 5. Submit crawl tasks recursively
        // 6. Wait for all tasks to complete
        // 7. Shutdown executor and return visited URLs

        // Helper method to extract hostname:
        // String getHostname(String url) {
        //     int start = url.indexOf("//") + 2;
        //     int end = url.indexOf('/', start);
        //     return end == -1 ? url.substring(start) : url.substring(start, end);
        // }

        throw new UnsupportedOperationException("Not implemented");
    }
}

// Mock HtmlParser for testing
class MockHtmlParser implements HtmlParser {
    private Map<String, List<String>> graph;

    public MockHtmlParser(Map<String, List<String>> graph) {
        this.graph = graph;
    }

    @Override
    public List<String> getUrls(String url) {
        return graph.getOrDefault(url, new ArrayList<>());
    }
}

class WebCrawlerMultithreadedTest {
    public static void main(String[] args) throws Exception {
        System.out.println("Testing Web Crawler Multithreaded...\n");

        // Test 1: Basic crawling
        System.out.println("Test 1: Basic crawling same hostname");
        Map<String, List<String>> graph1 = new HashMap<>();
        graph1.put("http://news.yahoo.com/news/topics/",
                   Arrays.asList("http://news.yahoo.com/news", "http://news.yahoo.com"));
        graph1.put("http://news.yahoo.com/news",
                   Arrays.asList("http://news.yahoo.com/news/topics/"));
        graph1.put("http://news.yahoo.com",
                   Arrays.asList("http://news.yahoo.com/us"));
        graph1.put("http://news.yahoo.com/us", new ArrayList<>());

        HtmlParser parser1 = new MockHtmlParser(graph1);
        WebCrawler crawler1 = new WebCrawler();
        List<String> result1 = crawler1.crawl("http://news.yahoo.com/news/topics/", parser1);

        Set<String> expected1 = new HashSet<>(Arrays.asList(
            "http://news.yahoo.com/news/topics/",
            "http://news.yahoo.com/news",
            "http://news.yahoo.com",
            "http://news.yahoo.com/us"
        ));
        assert new HashSet<>(result1).equals(expected1) : "Test 1 failed";
        System.out.println("✓ Test 1 passed\n");

        // Test 2: Different hostnames
        System.out.println("Test 2: Filter different hostname");
        Map<String, List<String>> graph2 = new HashMap<>();
        graph2.put("http://news.yahoo.com",
                   Arrays.asList("http://news.google.com", "http://news.yahoo.com/page"));
        graph2.put("http://news.yahoo.com/page", new ArrayList<>());
        graph2.put("http://news.google.com", Arrays.asList("http://news.google.com/page"));

        HtmlParser parser2 = new MockHtmlParser(graph2);
        WebCrawler crawler2 = new WebCrawler();
        List<String> result2 = crawler2.crawl("http://news.yahoo.com", parser2);

        Set<String> expected2 = new HashSet<>(Arrays.asList(
            "http://news.yahoo.com",
            "http://news.yahoo.com/page"
        ));
        assert new HashSet<>(result2).equals(expected2) : "Test 2 failed";
        assert !result2.contains("http://news.google.com") : "Test 2 failed: should not include google.com";
        System.out.println("✓ Test 2 passed\n");

        // Test 3: Cycle detection
        System.out.println("Test 3: Handle cycles");
        Map<String, List<String>> graph3 = new HashMap<>();
        graph3.put("http://example.com/a", Arrays.asList("http://example.com/b"));
        graph3.put("http://example.com/b", Arrays.asList("http://example.com/c"));
        graph3.put("http://example.com/c", Arrays.asList("http://example.com/a"));  // Cycle

        HtmlParser parser3 = new MockHtmlParser(graph3);
        WebCrawler crawler3 = new WebCrawler();
        List<String> result3 = crawler3.crawl("http://example.com/a", parser3);

        assert result3.size() == 3 : "Test 3 failed: should find exactly 3 URLs";
        System.out.println("✓ Test 3 passed\n");

        // Test 4: Single URL
        System.out.println("Test 4: Single URL with no links");
        Map<String, List<String>> graph4 = new HashMap<>();
        graph4.put("http://single.com", new ArrayList<>());

        HtmlParser parser4 = new MockHtmlParser(graph4);
        WebCrawler crawler4 = new WebCrawler();
        List<String> result4 = crawler4.crawl("http://single.com", parser4);

        assert result4.equals(Arrays.asList("http://single.com")) : "Test 4 failed";
        System.out.println("✓ Test 4 passed\n");

        System.out.println("All tests passed! ✓");
    }
}
