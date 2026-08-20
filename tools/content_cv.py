# -*- coding: utf-8 -*-
"""Icerik 1-Gorkem_Koc_CV_EN.pdf / 1-GorkemKoc_CV_TR.pdf metinlerinden alindi.
Iki dil ayni gercegi anlatir; sadece dil degisir."""

EN = {
 "lang": "en",
 "name": "Görkem Koç",
 "title": "Principal Specialist — System &amp; Infrastructure",
 "contact": "Ankara, Turkey&nbsp; ·&nbsp; gorkem.koc@ops-center.org&nbsp; ·&nbsp; "
            "cv.ops-center.org&nbsp; ·&nbsp; linkedin.com/in/grkmkoc",
 "page_word": "Page",
 "sections": [
  ("h", "Profile"),
  ("p", "System and infrastructure specialist with 7+ years in enterprise IT, currently Principal "
        "Specialist at Etiya after two promotions since 2021. I run hybrid identity across on-prem "
        "Active Directory and Microsoft 365 / Entra ID, manage the corporate endpoint estate with SCCM "
        "and ManageEngine, and keep business-critical services on VMware ESXi and Hyper-V resilient to a "
        "single-host failure. I translate ISO 27001 and PCI-DSS requirements into day-to-day operations "
        "and automate recurring work with Ansible and n8n. Completed the Architecting on AWS training in "
        "2025, with a growing focus on hybrid and cloud infrastructure."),

  ("h", "Experience"),
  ("job", {
    "role": "Principal Specialist — System &amp; Infrastructure",
    "meta": "Etiya · Ankara&nbsp; |&nbsp; 2021 – Present&nbsp; |&nbsp; System Support Specialist "
            "(Nov 2021 – Feb 2023) &#8594; Senior Specialist, System Support (Feb 2023 – Aug 2025) "
            "&#8594; Principal Specialist (Aug 2025 – Present)",
    "bullets": [
      "<b>Automated repetitive work.</b> Built n8n automation flows for recurring Jira requests such as "
      "new-hire onboarding, access requests and system needs. Steps that used to be handled manually now "
      "run automatically, so the team spends less time on routine tickets.",
      "<b>Brought company computers under centralized management.</b> Security updates and application "
      "installs for every company computer are deployed centrally via SCCM and ManageEngine, so every "
      "device is updated under the same policy at the same time.",
      "<b>Kept the server infrastructure available.</b> Configured VMware ESXi and Hyper-V so that a "
      "single host failure does not disrupt the service, keeping business-critical systems available "
      "during the day.",
      "<b>Moved user-account and email management to a hybrid model.</b> Integrated on-prem Active "
      "Directory with Microsoft 365 / Entra ID so they behave as a single identity infrastructure. An "
      "employee logs in with the same username from the office or from home, and all access is revoked "
      "in one move when someone leaves.",
      "<b>Brought security and compliance standards into daily operations.</b> Translated ISO 27001 and "
      "PCI-DSS requirements into daily operations: access rights are clearly defined per system, "
      "CrowdStrike and Trend Micro EDR are rolled out across all devices, and suspicious events are "
      "followed up on.",
      "<b>Migrated DNS to AWS Route 53.</b> Moved the company&#8217;s public DNS hosted zone from GoDaddy "
      "to AWS Route 53 and consolidated public DNS management on the AWS side.",
      "<b>Managed virtual servers on TTCloud.</b> Run the virtual servers in the TTCloud environment and "
      "automate their configuration and routine changes with Ansible, so setups stay consistent and "
      "repeatable.",
      "<b>Monitored the server estate.</b> Track servers with Grafana and FlowE to spot idle or "
      "underused machines and keep the environment efficient.",
    ],
    "tags": "Microsoft 365 · Entra ID · Active Directory · SCCM · ManageEngine · VMware ESXi · Hyper-V · "
            "Ansible · AWS Route 53 · TTCloud · Grafana · CrowdStrike · n8n · ISO 27001 · PCI-DSS",
  }),
  ("job", {
    "role": "Software Support Staff",
    "meta": "Akgün Bilgisayar A.Ş. — assigned to Çorum Chest Diseases Hospital&nbsp; |&nbsp; 2019 – 2021",
    "bullets": [
      "Monitored the Hospital Information System (HIS) and the underlying servers and addressed issues "
      "before they escalated, minimising disruption to the emergency and outpatient departments during "
      "the day.",
      "Set up regular backup policies with Veeam and Acronis and periodically tested that those backups "
      "could actually be restored, so data could be recovered after hardware failures.",
    ],
    "tags": "HIS · Veeam · Acronis · Backup &amp; restore testing",
  }),
  ("job", {
    "role": "IT Manager",
    "meta": "Apex Surgical Medical Center · Istanbul&nbsp; |&nbsp; Dec 2018 – May 2019",
    "bullets": [
      "Maintained the HP server and the Citrix environment running on it, through which users accessed "
      "shared applications from one place.",
      "Instead of installing the OS on every new computer one by one, built a network-based automatic "
      "deployment (WDS), so the same setup could be delivered to many computers at once.",
      "Segmented the local network into VLANs, separating patient-data traffic from guest/Wi-Fi traffic; "
      "the network became both safer and more orderly.",
      "Tracked the full hardware inventory, resolved incident tickets within target SLAs, and ran "
      "modernization projects for aging infrastructure components.",
    ],
    "tags": "HP Server · Citrix · WDS · WSUS · VLAN · SLA",
  }),

  ("h", "Technical Skills"),
  ("skills", [
    ("Cloud &amp; Microsoft 365", "Microsoft 365 Management, Azure AD (Entra ID), Exchange Online, "
                                  "Teams, VDI, AWS Route 53, TTCloud"),
    ("Windows Server",            "Active Directory (AD), GPO, DNS, DHCP, WDS, WSUS, PrintSrv, SCCM, "
                                  "ManageEngine, Windows Server 2012–2022"),
    ("Virtualization &amp; OS",   "VMware ESXi, Microsoft Hyper-V, KVM; Linux (RHEL / Ubuntu / CentOS), "
                                  "macOS"),
    ("Security &amp; compliance", "ISO 27001, PCI-DSS, CrowdStrike, Trend Micro"),
    ("Automation &amp; tooling",  "n8n, Ansible, Grafana, FlowE, Jira / Confluence, Veeam, Acronis"),
  ]),

  ("h", "Certifications"),
  ("list", [
    "Architecting on AWS · Edu Bulut · 2025",
    "ISO/IEC 27001:2022 Internal Auditor · Kalite Norm · 2024",
    "Linux System Administration · BlueMark Academy · 2022",
    "Udemy — Active Directory, SCCM, Virtualization (ESXi, Hyper-V, KVM)",
  ]),

  ("h", "Education"),
  ("list", [
    "Anadolu Üniversitesi · Labor Economics &amp; Industrial Relations · 2023 – 2025",
    "Bülent Ecevit Üniversitesi · Human Resources Management · 2016 – 2018",
    "Vocational High School · Information Technologies · 2013 – 2016",
  ]),

  ("h", "Languages"),
  ("list", ["Turkish — native&nbsp; ·&nbsp; English — Intermediate"]),
 ],
}

TR = {
 "lang": "tr",
 "name": "Görkem Koç",
 "title": "Principal Specialist — Sistem &amp; Altyapı",
 "contact": "Ankara, Türkiye&nbsp; ·&nbsp; gorkem.koc@ops-center.org&nbsp; ·&nbsp; "
            "cv.ops-center.org&nbsp; ·&nbsp; linkedin.com/in/grkmkoc",
 "page_word": "Sayfa",
 "sections": [
  ("h", "Özet"),
  ("p", "Kurumsal BT tarafında 7+ yıllık deneyimli sistem ve altyapı uzmanıyım; 2021&#8217;den bu yana "
        "Etiya&#8217;da iki terfiyle Principal Specialist olarak çalışıyorum. Şirket içi Active Directory "
        "ile Microsoft 365 / Entra ID&#8217;yi tek kimlik altyapısı olarak yönetiyor, kurumsal "
        "bilgisayarları SCCM ve ManageEngine ile merkezi yönetimde tutuyor, VMware ESXi ve Hyper-V "
        "üzerindeki iş-kritik servisleri tek host arızasına dayanıklı çalıştırıyorum. ISO 27001 ve "
        "PCI-DSS gereksinimlerini günlük operasyona taşıyor, tekrar eden işleri Ansible ve n8n ile "
        "otomatikleştiriyorum. 2025&#8217;te Architecting on AWS eğitimini tamamladım; hibrit ve bulut "
        "altyapı tarafına ağırlık veriyorum."),

  ("h", "İş Deneyimi"),
  ("job", {
    "role": "Principal Specialist — Sistem &amp; Altyapı",
    "meta": "Etiya · Ankara&nbsp; |&nbsp; 2021 – Halen&nbsp; |&nbsp; System Support Specialist "
            "(Kas 2021 – Şub 2023) &#8594; Senior Specialist, System Support (Şub 2023 – Ağu 2025) "
            "&#8594; Principal Specialist (Ağu 2025 – Halen)",
    "bullets": [
      "<b>İş akışı otomasyonu.</b> Tekrar eden Jira işlerini (yeni çalışan kurulumu, erişim talepleri, "
      "sistem ihtiyaçları) n8n ile otomasyona bağladım; eskiden elle yapılan adımlar artık otomatik "
      "tamamlanıyor, ekip rutin ticket&#8217;lara daha az zaman harcıyor.",
      "<b>Merkezi yönetim.</b> SCCM ve ManageEngine ile şirket bilgisayarlarını merkezi yönetime aldım; "
      "güvenlik güncellemeleri ve uygulama kurulumları tek politikayla merkezi olarak dağıtılıyor.",
      "<b>Sanallaştırma.</b> VMware ESXi ve Hyper-V üzerinde iş-kritik servisleri, tek bir host "
      "arızasının servisi durdurmayacağı şekilde yapılandırdım; sistemleri gün içinde erişilebilir "
      "tuttum.",
      "<b>Hibrit kimlik altyapısı.</b> Şirket içi Active Directory ile Microsoft 365 / Entra ID&#8217;yi "
      "entegre ederek tek kimlik altyapısı kurdum; çalışan ofisten de evden de aynı hesapla giriş "
      "yapıyor, ayrılışta erişim tek adımda kapanıyor.",
      "<b>Güvenlik ve uyumluluk.</b> ISO 27001 ve PCI-DSS gereksinimlerini günlük operasyona taşıdım: "
      "her sistem için erişim yetkilerini tanımladım, CrowdStrike ve Trend Micro EDR&#8217;ı tüm "
      "cihazlara yaydım ve şüpheli olayları takip ettim.",
      "<b>DNS&#8217;in AWS Route 53&#8217;e taşınması.</b> Şirketin public DNS hosted zone&#8217;unu "
      "GoDaddy&#8217;den AWS Route 53&#8217;e taşıdım ve public DNS yönetimini AWS tarafında topladım.",
      "<b>Sanal sunucu yönetimi (TTCloud).</b> TTCloud ortamındaki sanal sunucuları yönetiyorum; sunucu "
      "yapılandırmalarını ve rutin değişiklikleri Ansible ile otomatikleştiriyorum.",
      "<b>Sunucu izleme.</b> Sunucuları Grafana ve FlowE ile izliyorum; atıl (kullanılmayan) sunucuları "
      "tespit ederek ortamı verimli tutuyorum.",
    ],
    "tags": "Microsoft 365 · Entra ID · Active Directory · SCCM · ManageEngine · VMware ESXi · Hyper-V · "
            "Ansible · AWS Route 53 · TTCloud · Grafana · CrowdStrike · n8n · ISO 27001 · PCI-DSS",
  }),
  ("job", {
    "role": "Yazılım Destek Personeli",
    "meta": "Akgün Bilgisayar A.Ş. — Çorum Göğüs Hastalıkları Hastanesi sahasında&nbsp; |&nbsp; "
            "2019 – 2021",
    "bullets": [
      "HBYS ve bağlı sunucuları izledim; sorunları büyümeden, acil ve poliklinik birimlerini etkilemeden "
      "çözdüm.",
      "Veeam ve Acronis ile yedekleme politikaları kurdum; geri yükleme testlerini periyodik yaparak "
      "donanım arızalarında verinin kurtarılabilir kalmasını sağladım.",
    ],
    "tags": "HBYS · Veeam · Acronis · Geri yükleme testleri",
  }),
  ("job", {
    "role": "Bilgi İşlem Yöneticisi",
    "meta": "Apex Cerrahi Tıp Merkezi · İstanbul&nbsp; |&nbsp; Ara 2018 – May 2019",
    "bullets": [
      "HP sunucu üzerinde çalışan Citrix ortamını yönettim; kullanıcılar uygulamalara bu merkezi ortam "
      "üzerinden ortak erişti.",
      "WDS ile ağ tabanlı işletim sistemi dağıtımı kurdum; aynı kurulumu tek tek yüklemek yerine çok "
      "sayıda bilgisayara dağıttım.",
      "Yerel ağı VLAN&#8217;lara böldüm; hasta-veri trafiğini misafir/Wi-Fi trafiğinden ayırarak ağ "
      "güvenliğini artırdım.",
      "Donanım envanterini takip ettim, arızaları SLA hedefleri içinde çözdüm ve eskiyen altyapı için "
      "modernizasyon projeleri yürüttüm.",
    ],
    "tags": "HP Server · Citrix · WDS · WSUS · VLAN · SLA",
  }),

  ("h", "Teknik Yetkinlikler"),
  ("skills", [
    ("Bulut &amp; Microsoft 365", "Microsoft 365 Yönetimi, Azure AD (Entra ID), Exchange Online, Teams, "
                                  "VDI, AWS Route 53, TTCloud"),
    ("Windows Server",            "Active Directory (AD), GPO, DNS, DHCP, WDS, WSUS, PrintSrv, SCCM, "
                                  "ManageEngine, Windows Server 2012–2022"),
    ("Sanallaştırma &amp; OS",    "VMware ESXi, Microsoft Hyper-V, KVM; Linux (RHEL / Ubuntu / CentOS), "
                                  "macOS"),
    ("Güvenlik &amp; uyumluluk",  "ISO 27001, PCI-DSS, CrowdStrike, Trend Micro"),
    ("Otomasyon &amp; araçlar",   "n8n, Ansible, Grafana, FlowE, Jira / Confluence, Veeam, Acronis"),
  ]),

  ("h", "Sertifikalar"),
  ("list", [
    "Architecting on AWS · Edu Bulut · 2025",
    "ISO/IEC 27001:2022 Internal Auditor · Kalite Norm · 2024",
    "Linux System Administration · BlueMark Academy · 2022",
    "Udemy — Active Directory, SCCM, Sanallaştırma (ESXi, Hyper-V, KVM)",
  ]),

  ("h", "Eğitim"),
  ("list", [
    "Anadolu Üniversitesi · Çalışma Ekonomisi ve Endüstri İlişkileri · 2023 – 2025",
    "Bülent Ecevit Üniversitesi · İnsan Kaynakları Yönetimi · 2016 – 2018",
    "Endüstri Meslek Lisesi · Bilişim Teknolojileri · 2013 – 2016",
  ]),

  ("h", "Yabancı Dil"),
  ("list", ["Türkçe — ana dil&nbsp; ·&nbsp; İngilizce — Intermediate"]),
 ],
}
