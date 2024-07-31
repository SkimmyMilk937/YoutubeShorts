import praw
import argparse
import xml.etree.cElementTree as et
import google.generativeai as genai
import os
import sys
import time

# subs = ["wallstreetbets", "finance"] #subreddits to be added

# querys = ["Mortgage", "Interest Rate", "Down Payment", "Credit Score", "Pre-Approval", 
#           "Closing Costs","Real Estate Agent","Home Inspection","Appraisal",
#           "Homeowners Insurance","Property Taxes","Escrow","Offer", "Negotiation",
#           "Title","Loan","Equity","FHA Loan","Conventional Loan","Debt-to-Income Ratio"] #search query terms, finds one per post
def main(numPosts):
    dir = os.getcwd()
    nums = int(numPosts)

    GOOGLE_API_KEY=('AIzaSyCJimkb03lG8bCulitXA4dJfwzz07jyMSk')
    genai.configure(api_key=GOOGLE_API_KEY)


    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    
    reddit = praw.Reddit(client_id="Q9ype9vp1GaCjbGAL_XG5Q", 
                            client_secret="FHJ9XHwxdHXk3Cq1K6ZKBPZpOnSqPw",
                            user_agent="Scraper",
                            username="ThatMortgageMan",
                            password="Mr.Mortgage"
                            )
    
    try:
        subs = open("subreddits.txt", "r").read().splitlines()
        querys = open("querys.txt", "r").read().splitlines()
        ids = open("postIDS.txt", "r").read().splitlines()
        message = open("message.txt", "r").read()
    except:
        print("Text files are not written :(")
        print("Please fill them in now and then try again")
        sys.exit()

    
    for x in subs:
        subreddit = reddit.subreddit(x)
        root = et.Element(subreddit.title)
        for quest in querys:
            for post in subreddit.search(query=quest, sort="new", limit=nums):
                if "?" in post.title and not(post.stickied) and not(post.id in ids):
                    f = open(f"{dir}/postIDS.txt", "a")
                    submission = reddit.submission(post.id)
                    f.write(post.id + "\n")
                    f.close()
                    
                        
                    f = open(f"{dir}/log.txt", "a")
                    f.write(f"Written to postIDLIST: {post.id}\n")
                    f.write("Read message from message.txt\n")
                    #reddit.redditor(submission.author.name).message(subject=f"Hello!)", message=message) #message
                    f.write(f"sent message to redditor: {post.author.name}\n")
                    response = model.generate_content(post.title)
                    #submission.reply(response.text) #comment response
                    f.write(f"replied to post: {post.id}\n")
                    
                    # listing = et.SubElement(root, "title", title=post.title)
                    # et.SubElement(listing, "text", text=post.selftext)
                    # tree = et.ElementTree(root)
                    # tree.write(f"{dir}/{x}.xml")
                else:
                    nums+=1
                    continue
                time.sleep(20)
                



    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--numPosts", help="how many posts to record", required=True)
    args = parser.parse_args()

    main( args.numPosts)
    print("Complete")