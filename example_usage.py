from client import UgcCreatorBriefAuctionMatchmakerClient

def main():
    client = UgcCreatorBriefAuctionMatchmakerClient()
    res = client.match_ugc_creators_for_brief('Organic Skincare Glow Serum Review', 200.00, 3)
    print('UGC Brief Auction Matchmaker: ' + res['brief_auction_id'] + ' (' + res['brief_title'] + ')')
    print('Matched Creators: ' + str(res['creators_matched_and_accepted_count']) + ' | Avg Bid: $' + str(res['average_creator_bid_usd']))
    print('Total Spend: $' + str(res['total_committed_campaign_spend_usd']))
    print('Auction Portal: ' + res['brief_bidding_auction_portal_url'])

if __name__ == '__main__':
    main()
