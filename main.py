import json

def load_ytd(path):
    """Return the data stored in one archive .js file."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    eq_index = content.find('=')
    
    if eq_index != -1:
        json_str = content[eq_index + 1:].strip()
        if json_str.endswith(';'):
            json_str = json_str[:-1]
        return json.loads(json_str)
        
    return json.loads(content)

# You will write your loops down here during class!



ad_data = load_ytd("data/ad-engagements.js")

seen_ads = set()      # distinct tweet IDs with Keywords targeting
advertisers = set()   # distinct advertisers who used it
ads_per_advertiser = {}

for item in ad_data:
    for entry in item["ad"]["adsUserData"]["adEngagements"]["engagements"]:
        imp = entry["impressionAttributes"]

        # keep only ads with a "Keywords" targeting criterion
        has_keywords = False
        for criterion in imp.get("matchedTargetingCriteria", []):
            if criterion.get("targetingType") == "Keywords":
                has_keywords = True
                break
        if not has_keywords:
            continue

        promo = imp.get("promotedTweetInfo")
        if not promo or not promo.get("tweetId"):
            continue

        tweet_id = promo["tweetId"]
        advertiser = imp["advertiserInfo"]["advertiserName"]

        advertisers.add(advertiser)
        if tweet_id not in seen_ads:          # count each ad once
            seen_ads.add(tweet_id)
            ads_per_advertiser[advertiser] = ads_per_advertiser.get(advertiser, 0) + 1

print("a:", len(seen_ads))
print("b:", len(advertisers))
print("c:", max(ads_per_advertiser, key=ads_per_advertiser.get))
