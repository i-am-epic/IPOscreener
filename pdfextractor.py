import re
from pdfscrapper import extract_text_from_pdf


def extract_ipo_data_from_pdf(pdf_text):
    """
    Extract IPO-related data from text extracted from a PDF.

    Parameters:
    - pdf_text (str): Text extracted from a PDF.

    Returns:
    - dict: Extracted IPO data.
    """
    extracted_data = {}

    # Define regex patterns for parameter extraction
    patterns = {
        "ipoSize": r"IPO\s*Size\s*:\s*([^\n]+)",
        "freshIssueVsOfferForSale": r"Fresh\s*Issue\s*:\s*([^\n]+)\s*Offer\s*for\s*Sale\s*:\s*([^\n]+)",
        "subscriptionRate": r"Subscription\s*Rate\s*:\s*([^\n]+)",
        "listingDate": r"Listing\s*Date\s*:\s*([^\n]+)",
        "priceBand": r"Price\s*Band\s*:\s*([^\n]+)",
        "lotSize": r"Lot\s*Size\s*:\s*([^\n]+)",
        "totalIssueSize": r"Total\s*Issue\s*Size\s*:\s*([^\n]+)",
        "issueType": r"Issue\s*Type\s*:\s*([^\n]+)",
        "listingAt": r"Listing\s*At\s*:\s*([^\n]+)",
        "shareHoldingPreIssue": r"Share\s*holding\s*pre\s*issue\s*:\s*([^\n]+)",
        "shareHoldingPostIssue": r"Share\s*holding\s*post\s*issue\s*:\s*([^\n]+)",
        # Add other parameters similarly
    }

    for parameter, pattern in patterns.items():
        match = re.search(pattern, pdf_text, re.IGNORECASE)
        extracted_data[parameter] = match.group(1).strip() if match else None

    return extracted_data

# Example Usage
pdf_path = '1699876097528.pdf'
pdf_text = extract_text_from_pdf(pdf_path)
ipo_data = extract_ipo_data_from_pdf(pdf_text)
print(ipo_data)
