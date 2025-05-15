import requests
from bs4 import BeautifulSoup
import pandas as pd
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# websites = ["https://nogood.io", "https://hunterdigitalmarketing.com", "https://fishbat.com", "https://aumcore.com", "https://thriveagency.com", "https://boucherco.com", "https://digitalsilk.com", "https://hubspot.com", "https://clutch.co", "https://linkedin.com", "https://webfx.com", "https://jivesmedia.com", "https://succeedingsmall.co", "https://found.co.uk", "https://wishagency.co.uk", "https://designrush.com", "https://wpromote.com", "https://nydigitalawards.com", "https://semrush.com", "https://mackmediagroup.com", "https://digitalagencynetwork.com", "https://ninjapromo.io", "https://terrahq.com", "https://imarkinfotech.com", "https://inbeat.agency", "https://builtinnyc.com", "https://improvado.io", "https://goodfirms.co", "https://lifesight.io", "https://thesocialshepherd.com", "https://tugagency.com", "https://sortlist.com", "https://bird.marketing", "https://chatterbuzzmedia.com", "https://voymedia.com", "https://vmgroupe.com", "https://stramasa.com", "https://mediaforce.ca", "https://socialflyny.com", "https://frshlabs.co", "https://thecharlesnyc.com", "https://digitalcrew.agency", "https://advancemediany.com", "https://kobedigital.com", "https://verbszmarketing.com", "https://adlift.com", "https://acadium.com", "https://pixelcrayons.com", "https://agencyspotter.com", "https://lyfemarketing.com", "https://taktical.co", "https://matebiz.com", "https://copify.com", "https://yelp.com", "https://brandloom.com", "https://2pointagency.com", "https://topdevelopers.co", "https://vaynermedia.com", "https://weboin.com", "https://dotyeti.com", "https://mcsaatchiperformance.com", "https://digitalnycagency.com", "https://influencermarketinghub.com", "https://aerobusinesssolutions.com", "https://yourdigitalresource.com", "https://upcity.com", "https://dmthriveagency.com", "https://inbeat.co", "https://ddb.com", "https://outsourceaccelerator.com", "https://growth-hackers.net", "https://manifest.com", "https://themanifest.com", "https://topagency.com", "https://busyseed.com", "https://maxburst.com", "https://bbdo.com", "https://indeedseo.com", "https://43oak.com", "https://disruptiveadvertising.com", "https://jpost.com", "https://aka.nyc", "https://peertopeermarketing.co", "https://grey.com", "https://f6s.com", "https://capterra.com", "https://scottmax.com", "https://smartsites.com", "https://instagram.com", "https://thedrum.com", "https://jellyfish.com", "https://omnicomgroup.com", "https://wikipedia.org", "https://jake-jorgovan.com", "https://storychief.io", "https://ogilvy.com"]
# websites = ["https://www.chariotsforhire.com", "https://www.williamsburgchauffeur.com", "https://www.tripadvisor.in", "https://www.luxviptransportation.com", "https://royalairportconcierge.com", "https://www.airportassist.com", "https://www.dclivery.com", "https://virginia-limousine.com", "https://www.albemarlelimousine.com", "https://tavoperationservices.com", "https://theabroadguide.com", "https://airportselect.com", "https://www.expedia.com", "https://www.vaexecutivesedan.com", "https://executivecarusa.com", "https://overthetoplimousine.com", "https://www.rmalimo.com", "https://www.execucar.com", "https://atouchofclasslimousines.com", "https://rdvlimo.com", "https://www.primetimeshuttle.com", "https://www.marrowtransit.com", "https://richmondlimo.com", "https://www.norfolkairport.com", "https://www.newdelhiairport.in", "http://karachiairportassistance.com", "https://www.aena.es", "https://dcacar.com", "https://intomason.gmu.edu", "https://www.visitvirginiabeach.com", "https://www.marhabaservices.com", "https://www.flydulles.com", "https://www.flygreet.com", "https://limo.wadialghaf.com", "https://www.empirecls.com", "https://www.pearlassist.com", "https://www.carey.com", "https://www.madisonlimous.com", "https://www.bark.com", "https://robbreport.com", "https://virginia.limo", "https://www.flyreagan.com", "https://www.beniconnect.com", "https://www.inglimo.com", "https://www.supershuttle.com", "https://www.restonlimo.com", "https://www.mwaa.com", "https://www.tsa.gov", "https://www.jameslimousine.com", "https://flyfrompti.com", "https://a1andedencars.co.uk", "https://www.lukebryan.com", "https://www.carmellimo.com", "https://pearlassist.com", "https://www.rideinbliss.com", "https://www.saudia.com", "https://www.manchesterairport.co.uk", "https://www.oleta.com", "https://www.honorflight.org", "https://www.wboy.com", "https://azeelimoservice.com", "https://blackcareverywhere.com", "https://www.basilicasanpietro.va", "https://www.goldcoastairport.com.au", "https://www.blueangels.navy.mil", "https://www.tripadvisor.com.vn", "https://gmtravelsolution.com", "https://www.delta.com", "https://careers.virginatlantic.com", "https://senatetransportationservices.com", "https://www.lukecombs.com", "https://www.emirates.com", "https://welcomecorps.org", "https://www.summitbsa.org", "https://www.jble.af.mil", "https://www.skywest.com", "https://www.yelp.com", "https://www.pgatoursuperstore.com", "https://www.opulencetransportation.com", "https://www.dogtopia.com", "https://airporttransfer.com", "https://noblecrownlimo.com", "https://www.wvtf.org", "https://flysrq.com", "https://www.mtnlakelodge.com", "https://www.samsung.com", "https://www.aceairports.com", "https://uk.trustpilot.com"]

# roofing and construction austin texas
websites = ["https://accurateroofingaustin.com", "https://actionroofingaustin.com", "https://alliedsidingandwindows.com"]

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

social_domains = {
    "linkedin.com": "LinkedIn",
    "twitter.com": "Twitter",
    "facebook.com": "Facebook",
    "instagram.com": "Instagram",
    "youtube.com": "YouTube",
    "tiktok.com": "TikTok",
    "pinterest.com": "Pinterest",
    "threads.net": "Threads"
}

session = requests.Session()
retries = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)
session.mount("https://", HTTPAdapter(max_retries=retries))
session.headers.update(HEADERS)

def extract_social_links(url):
    try:
        response = session.get(url, timeout=15)
        soup = BeautifulSoup(response.text, "html.parser")
        found = {name: "" for name in social_domains.values()}
        for a in soup.find_all("a", href=True):
            href = a["href"]
            for domain, name in social_domains.items():
                if domain in href:
                    found[name] = href
        return found
    except Exception as e:
        print(f"[Error] {url} -> {e}")
        return {name: "" for name in social_domains.values()}

rows = []
for site in websites:
    print(f"Crawling: {site}")
    socials = extract_social_links(site)
    row = {"Website": site}
    row.update(socials)
    rows.append(row)

df = pd.DataFrame(rows)
df.to_excel("social_links.xlsx", index=False)
print("\n✅ Data saved to social_links.xlsx")
