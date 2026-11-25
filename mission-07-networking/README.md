# Mission 7 — How Computers Communicate

## 1. Task / objective
Explain fundamental networking concepts (LAN, MAN, WAN, DNS, router, protocol, packet switching, client-server), observe connectivity and DNS lookup results safely in Terminal, and describe step by step what happens when a website opens.

## 2. Work completed
- Completed the network concepts table with plain-language explanations and concrete examples.
- Ran `ping -c 3 example.com` to test reachability and `dig example.com +noall +answer` to observe DNS resolution without exposing any local IP address or Wi-Fi details.
- Wrote a 6-step explanation of how a browser loads a web page using the terms client, server, DNS, and protocol.

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| --- | --- | --- |
| LAN | A network covering a small local area, such as a home, classroom, or office. | Devices connected to the same home Wi-Fi router. |
| MAN | A network spanning a city or large university campus. | A city-wide municipal fiber network connecting multiple campus buildings. |
| WAN | A network covering large geographical distances across cities or countries. | The global internet connecting regional networks worldwide. |
| DNS | The naming system that translates human-friendly domain names into numeric IP addresses. | Resolving `example.com` to `104.20.23.154`. |
| Router | A networking device that connects separate networks and forwards packets toward their destination. | A home router forwarding traffic between your LAN and your ISP's WAN. |
| Protocol | An agreed-upon set of rules and formats that devices follow to exchange data reliably. | HTTPS / HTTP for web pages, or TCP/IP for packet delivery. |
| Packet switching | Splitting messages into small packets that travel independently across the network and are reassembled at the destination. | Sending a web page as multiple IP packets across internet routers. |
| Client-server | A communication model where a client requests a resource or service and a server responds with it. | A web browser (client) requesting a page from a web server. |

### Task 7.2 — Observe network information
- **Connectivity test (`ping -c 3 example.com`):** Transmitted 3 ICMP echo packets to `example.com` (`104.20.23.154`), received 3 replies with `0.0% packet loss` and an average round-trip time of `4.203 ms`.
- **DNS lookup (`dig example.com +noall +answer`):** Returned two `A` records (`172.66.147.243` and `104.20.23.154`) with a TTL of `98` seconds.
- **What a connectivity test checks:** It verifies whether a remote host is reachable over the network, whether packets are being dropped, and how long a round trip takes.
- **What a DNS lookup displays:** It shows the DNS record type (such as `A` for IPv4 addresses), the time-to-live (TTL), and the public IP address(es) mapped to the domain name.
- **Role of DNS when entering a website name:** Computers route traffic using IP addresses rather than words, so DNS automatically translates the domain name you type into the server's IP address before the browser connects.

### Task 7.3 — What happens when you open a website?
1. You type a URL such as `https://example.com` into your web browser, which acts as the **client**.
2. Because the browser needs a numeric IP address to contact the destination, it sends a query to **DNS** to translate `example.com` into an IP address (such as `104.20.23.154`).
3. Using that IP address, the client's request is broken into packets and sent through your local **router** and across ISP networks toward the destination network.
4. The client establishes a connection with the remote web **server** and sends an HTTP/HTTPS request following the rules of that **protocol**.
5. The **server** processes the request and sends back an HTTP/HTTPS response containing the status code and web page data (HTML, CSS, and assets) as packets.
6. Your browser (the **client**) reassembles the response packets and renders the web page on your screen.

## 3. Commands / tools used
- `ping -c 3 example.com`: Tested network reachability and round-trip latency to a public example domain.
- `dig example.com +noall +answer`: Performed a DNS lookup to inspect public `A` records without exposing local resolver or personal IP details.
- `git add`, `git commit`, `git push`: Recorded and published Mission 7 to GitHub.

## 4. My understanding
Loading a website relies on multiple layers working together: DNS translates names to IP addresses, routers forward packets across interconnected networks, and standard protocols like TCP/IP and HTTPS let the client browser and remote server exchange data reliably.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [README.md](README.md)
- [../evidence/mission-07-network.txt](../evidence/mission-07-network.txt)

## 8. Commit details
- Commit message: `Explain networking concepts and website communication`
- Pushed to `origin/main` on GitHub and verified.
