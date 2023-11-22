import requests
from bs4 import BeautifulSoup
import json

def get_parameter_value(soup, parameter_name):
    if parameter_name == "ipoSize":
        return extract_ipo_size(soup)
    elif parameter_name == "freshIssueVsOfferForSale":
        return extract_fresh_issue_vs_offer_for_sale(soup)
    elif parameter_name == "subscriptionRate":
        return extract_subscription_rate(soup)
    elif parameter_name == "listingDate":
        return extract_listing_date(soup)
    elif parameter_name == "priceBand":
        return extract_price_band(soup)
    elif parameter_name == "lotSize":
        return extract_lot_size(soup)
    elif parameter_name == "totalIssueSize":
        return extract_total_issue_size(soup)
    elif parameter_name == "issueType":
        return extract_issue_type(soup)
    elif parameter_name == "listingAt":
        return extract_listing_at(soup)
    elif parameter_name == "shareHoldingPreIssue":
        return extract_share_holding_pre_issue(soup)
    elif parameter_name == "shareHoldingPostIssue":
        return extract_share_holding_post_issue(soup)
    # Add other parameters similarly

def extract_ipo_size(soup):
    total_issue_size_element = soup.select_one('td:contains("Total Issue Size") + td')
    return total_issue_size_element.text.strip() if total_issue_size_element else None

def extract_fresh_issue_vs_offer_for_sale(soup):
    fresh_issue_element = soup.select_one('td:contains("Fresh Issue") + td')
    offer_for_sale_element = soup.select_one('td:contains("Offer for Sale") + td')
    
    if fresh_issue_element and offer_for_sale_element:
        fresh_issue = fresh_issue_element.text.strip()
        offer_for_sale = offer_for_sale_element.text.strip()
        return f"{fresh_issue} vs {offer_for_sale}"
    
    return None

def extract_subscription_rate(soup):
    subscription_rate_element = soup.select_one('td:contains("Subscription Rate") + td')
    return subscription_rate_element.text.strip() if subscription_rate_element else None

def extract_listing_date(soup):
    listing_date_element = soup.select_one('td:contains("Listing Date") + td')
    return listing_date_element.text.strip() if listing_date_element else None

def extract_price_band(soup):
    price_band_element = soup.select_one('td:contains("Price Band") + td')
    return price_band_element.text.strip() if price_band_element else None

def extract_lot_size(soup):
    lot_size_element = soup.select_one('td:contains("Lot Size") + td')
    return lot_size_element.text.strip() if lot_size_element else None

def extract_total_issue_size(soup):
    total_issue_size_element = soup.select_one('td:contains("Total Issue Size") + td')
    return total_issue_size_element.text.strip() if total_issue_size_element else None

def extract_issue_type(soup):
    issue_type_element = soup.select_one('td:contains("Issue Type") + td')
    return issue_type_element.text.strip() if issue_type_element else None

def extract_listing_at(soup):
    listing_at_element = soup.select_one('td:contains("Listing At") + td')
    return listing_at_element.text.strip() if listing_at_element else None

def extract_share_holding_pre_issue(soup):
    share_holding_pre_issue_element = soup.select_one('td:contains("Share holding pre issue") + td')
    return share_holding_pre_issue_element.text.strip() if share_holding_pre_issue_element else None

def extract_share_holding_post_issue(soup):
    share_holding_post_issue_element = soup.select_one('td:contains("Share holding post issue") + td')
    return share_holding_post_issue_element.text.strip() if share_holding_post_issue_element else None


# Function to extract IPO details from a website
def scrape_ipo_details(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data based on HTML structure (replace with actual HTML structure)
        revenue_growth = get_parameter_value(soup, "revenueGrowth")
        profit_margin = get_parameter_value(soup, "profitMargin")
        debt_to_equity_ratio = get_parameter_value(soup, "debtToEquityRatio")
        market_position = get_parameter_value(soup, "marketPosition")
        industry_growth_prospects = get_parameter_value(soup, "industryGrowthProspects")
        promoter_holding = get_parameter_value(soup, "promoterHolding")
        corporate_governance = get_parameter_value(soup, "corporateGovernance")
        ipo_size = get_parameter_value(soup, "ipoSize")
        fresh_issue_vs_offer_for_sale = get_parameter_value(soup, "freshIssueVsOfferForSale")
        subscription_rate = get_parameter_value(soup, "subscriptionRate")
        management_track_record = get_parameter_value(soup, "managementTrackRecord")
        key_executive_experience = get_parameter_value(soup, "keyExecutiveExperience")
        price_to_earnings_ratio = get_parameter_value(soup, "priceToEarningsRatio")
        market_capitalization = get_parameter_value(soup, "marketCapitalization")
        return_on_equity = get_parameter_value(soup, "returnOnEquity")
        earnings_per_share = get_parameter_value(soup, "earningsPerShare")
        inventory_turnover = get_parameter_value(soup, "inventoryTurnover")
        asset_turnover = get_parameter_value(soup, "assetTurnover")
        operating_cash_flow = get_parameter_value(soup, "operatingCashFlow")
        free_cash_flow = get_parameter_value(soup, "freeCashFlow")
        legal_history = get_parameter_value(soup, "legalHistory")
        regulatory_violations = get_parameter_value(soup, "regulatoryViolations")
        volatility_analysis = get_parameter_value(soup, "volatilityAnalysis")
        external_risks = get_parameter_value(soup, "externalRisks")
        economic_climate = get_parameter_value(soup, "economicClimate")
        investor_sentiment = get_parameter_value(soup, "investorSentiment")
        reputation_of_underwriters = get_parameter_value(soup, "reputationOfUnderwriters")
        underwriter_track_record = get_parameter_value(soup, "underwriterTrackRecord")
        trading_volume = get_parameter_value(soup, "tradingVolume")
        price_volatility = get_parameter_value(soup, "priceVolatility")
        insider_selling = get_parameter_value(soup, "insiderSelling")
        lock_up_expiry = get_parameter_value(soup, "lockUpExpiry")
        rating_agencies_assessment = get_parameter_value(soup, "ratingAgenciesAssessment")
        consensus_analyst_ratings = get_parameter_value(soup, "consensusAnalystRatings")
        investor_relations = get_parameter_value(soup, "investorRelations")
        transparency_in_disclosures = get_parameter_value(soup, "transparencyInDisclosures")
        historical_ipo_performance = get_parameter_value(soup, "historicalIpoPerformance")
        post_ipo_stock_performance = get_parameter_value(soup, "postIpoStockPerformance")
        industry_peers_performance = get_parameter_value(soup, "industryPeersPerformance")
        market_share_comparison = get_parameter_value(soup, "marketShareComparison")
        institutional_ownership = get_parameter_value(soup, "institutionalOwnership")
        anchor_investor_participation = get_parameter_value(soup, "anchorInvestorParticipation")
        promoter_lock_in = get_parameter_value(soup, "promoterLockIn")
        employee_lock_in = get_parameter_value(soup, "employeeLockIn")
        clarity_in_fund_utilization = get_parameter_value(soup, "clarityInFundUtilization")
        alignment_with_business_goals = get_parameter_value(soup, "alignmentWithBusinessGoals")
        roadshow_effectiveness = get_parameter_value(soup, "roadshowEffectiveness")
        public_awareness_initiatives = get_parameter_value(soup, "publicAwarenessInitiatives")
        investor_services = get_parameter_value(soup, "investorServices")
        post_ipo_communications = get_parameter_value(soup, "postIpoCommunications")

        # Create a dictionary to store the extracted data
        scraped_data = {
            "ipoDetails": {
                "financialHealth": {
                    "revenueGrowth": revenue_growth,
                    "profitMargin": profit_margin,
                    "debtToEquityRatio": debt_to_equity_ratio
                },
                "marketAndIndustryAnalysis": {
                    "marketPosition": market_position,
                    "industryGrowthProspects": industry_growth_prospects
                },
                "companyInformationAndGovernance": {
                    "promoterHolding": promoter_holding,
                    "corporateGovernance": corporate_governance
                },
                "ipoSpecifics": {
                    "ipoSize": ipo_size,
                    "freshIssueVsOfferForSale": fresh_issue_vs_offer_for_sale
                },
                "subscriptionMetrics": {
                    "subscriptionRate": subscription_rate,
                    "retailInvestorInterest": None  # Add logic for retail investor interest
                },
                "managementAndLeadership": {
                    "managementTrackRecord": management_track_record,
                    "keyExecutiveExperience": key_executive_experience
                },
                "valuationMetrics": {
                    "priceToEarningsRatio": price_to_earnings_ratio,
                    "marketCapitalization": market_capitalization
                },
                "financialRatios": {
                    "returnOnEquity": return_on_equity,
                    "earningsPerShare": earnings_per_share
                },
                "operationalEfficiency": {
                    "inventoryTurnover": inventory_turnover,
                    "assetTurnover": asset_turnover
                },
                "cashFlowManagement": {
                    "operatingCashFlow": operating_cash_flow,
                    "freeCashFlow": free_cash_flow
                },
                "regulatoryCompliance": {
                    "legalHistory": legal_history,
                    "regulatoryViolations": regulatory_violations
                },
                "riskAnalysis": {
                    "volatilityAnalysis": volatility_analysis,
                    "externalRisks": external_risks
                },
                "marketConditions": {
                    "economicClimate": economic_climate,
                    "investorSentiment": investor_sentiment
                },
                "underwritingAndAdvisory": {
                    "reputationOfUnderwriters": reputation_of_underwriters,
                    "underwriterTrackRecord": underwriter_track_record
                },
                "postIpoLiquidity": {
                    "tradingVolume": trading_volume,
                    "priceVolatility": price_volatility
                },
                "lockUpPeriod": {
                    "insiderSelling": insider_selling,
                    "lockUpExpiry": lock_up_expiry
                },
                "ipoGrading": {
                    "ratingAgenciesAssessment": rating_agencies_assessment,
                    "consensusAnalystRatings": consensus_analyst_ratings
                },
                "communicationAndTransparency": {
                    "investorRelations": investor_relations,
                    "transparencyInDisclosures": transparency_in_disclosures
                },
                "postIpoPerformance": {
                    "historicalIpoPerformance": historical_ipo_performance,
                    "postIpoStockPerformance": post_ipo_stock_performance
                },
                "peerComparison": {
                    "industryPeersPerformance": industry_peers_performance,
                    "marketShareComparison": market_share_comparison
                },
                "institutionalInvestors": {
                    "institutionalOwnership": institutional_ownership,
                    "anchorInvestorParticipation": anchor_investor_participation
                },
                "lockInPeriods": {
                    "promoterLockIn": promoter_lock_in,
                    "employeeLockIn": employee_lock_in
                },
                "objectivesOfTheIssue": {
                    "clarityInFundUtilization": clarity_in_fund_utilization,
                    "alignmentWithBusinessGoals": alignment_with_business_goals
                },
                "investorEducationAndAwareness": {
                    "roadshowEffectiveness": roadshow_effectiveness,
                    "publicAwarenessInitiatives": public_awareness_initiatives
                },
                "postIpoSupport": {
                    "investorServices": investor_services,
                    "postIpoCommunications": post_ipo_communications
                }
            }
        }

        # Convert the dictionary to a JSON string
        json_data = json.dumps(scraped_data, indent=2)
        return json_data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Example usage
url = 'https://www.chittorgarh.com/ipo/ireda-ipo/1569/'
json_data = scrape_ipo_details(url)

if json_data:
    print(json_data)
