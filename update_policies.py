import os

layout = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{TITLE} - Healthy Today Store</title>
    <style>
        :root {
            --primary: #047857; /* Emerald 700 */
            --primary-hover: #065f46;
            --bg-color: #f8fafc;
            --card-bg: #ffffff;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --border: #e2e8f0;
            --accent: #f59e0b;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            overflow-x: hidden;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--primary);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .cart-icon {
            position: relative;
            cursor: pointer;
        }
        
        .cart-count {
            position: absolute;
            top: -8px;
            right: -8px;
            background: var(--accent);
            color: white;
            font-size: 0.7rem;
            font-weight: bold;
            padding: 2px 6px;
            border-radius: 10px;
        }

        .footer-links a {
            color: #94a3b8;
            text-decoration: none;
        }

        /* Responsive Fixes */
        .search-bar-container {
            display: none;
        }

        @media (min-width: 768px) {
            .search-bar-container {
                display: block;
                flex: 1;
                max-width: 500px;
                margin: 0 20px;
            }
        }
        
        .page-content {
            flex: 1;
            max-width: 800px;
            margin: 40px auto;
            padding: 40px;
            background: #fff;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
            line-height: 1.6;
            color: #334155;
        }
        .page-content h1 {
            color: #0f172a;
            font-size: 2.2rem;
            margin-bottom: 20px;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 10px;
        }
        .page-content h2 {
            color: #0f172a;
            margin-top: 30px;
            margin-bottom: 15px;
            font-size: 1.4rem;
        }
        .page-content p {
            margin-bottom: 15px;
            font-size: 1.05rem;
        }
        .page-content ul {
            margin-left: 20px;
            margin-bottom: 15px;
            font-size: 1.05rem;
        }
    </style>
</head>
<body>

    <div style="background: #064e3b; color: white; text-align: center; padding: 8px; font-size: 0.85rem; font-weight: 600; letter-spacing: 0.5px;">
        🔥 FREE US SHIPPING ON ORDERS OVER $99 | 100% SATISFACTION GUARANTEE
    </div>
    <header style="background: #fff; padding: 15px 20px; display: flex; flex-direction: column; gap: 15px; border-bottom: 1px solid #e2e8f0;">
        <div style="display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto; width: 100%;">
            <a href="index.html" class="logo" style="font-size: 1.8rem;">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg>
                Healthy Today Store
            </a>
            <div class="search-bar-container">
                <div style="position: relative;">
                    <input type="text" placeholder="Search for supplements, vitamins..." style="width: 100%; padding: 10px 15px; border-radius: 20px; border: 1px solid #cbd5e1; outline: none; box-shadow: inset 0 1px 2px rgba(0,0,0,0.05);">
                    <svg style="position: absolute; right: 15px; top: 10px;" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                </div>
            </div>
            <div class="cart-icon">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#334155" stroke-width="2"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
                <span class="cart-count" style="background: #ef4444;">1</span>
            </div>
        </div>
        <nav style="display: flex; justify-content: center; gap: 25px; font-size: 0.9rem; font-weight: 600; color: #475569; border-top: 1px solid #f1f5f9; padding-top: 12px; max-width: 1200px; margin: 0 auto; width: 100%; overflow-x: auto; white-space: nowrap;">
            <a href="index.html" style="text-decoration: none; color: inherit;">Vitamins</a>
            <a href="index.html" style="text-decoration: none; color: inherit;">Weight Loss</a>
            <a href="index.html" style="text-decoration: none; color: inherit;">Men's Health</a>
            <a href="index.html" style="text-decoration: none; color: inherit;">Women's Health</a>
            <a href="index.html" style="text-decoration: none; color: #059669;">Best Sellers</a>
        </nav>
    </header>

    <div class="page-content">
        {CONTENT}
    </div>

    <footer style="background: #0f172a; color: #94a3b8; padding: 50px 20px 20px; font-size: 0.85rem;">
        <div style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px; margin-bottom: 40px;">
            <div>
                <h3 style="color: #fff; font-size: 1.1rem; margin-bottom: 15px; font-weight: 600;">About Healthy Today Store</h3>
                <p style="line-height: 1.6;">Your #1 Trusted Retailer for premium dietary supplements. We guarantee 100% authentic products sourced directly from FDA-registered facilities.</p>
            </div>
            <div>
                <h3 style="color: #fff; font-size: 1.1rem; margin-bottom: 15px; font-weight: 600;">Customer Support</h3>
                <p style="margin-bottom: 8px;">📞 1-800-555-0199 (Toll-Free)</p>
                <p style="margin-bottom: 8px;">✉️ support@healthytodaystore.com</p>
                <p>🏢 1204 Health Ave, Suite 300<br>Wilmington, DE 19801, USA</p>
            </div>
            <div>
                <h3 style="color: #fff; font-size: 1.1rem; margin-bottom: 15px; font-weight: 600;">Secure Shopping</h3>
                <div style="display: flex; gap: 10px; margin-bottom: 15px; font-weight: bold; color: #fff;">
                    <span>VISA</span> | <span>MC</span> | <span>AMEX</span> | <span>DISCOVER</span>
                </div>
                <div style="display: flex; gap: 10px;">
                    <div style="border: 1px solid #334155; padding: 5px 10px; border-radius: 4px; display: flex; align-items: center; gap: 5px;">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg> Norton Secured
                    </div>
                    <div style="border: 1px solid #334155; padding: 5px 10px; border-radius: 4px; display: flex; align-items: center; gap: 5px;">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg> McAfee Secure
                    </div>
                </div>
            </div>
        </div>
        <div style="border-top: 1px solid #1e293b; padding-top: 20px; display: flex; flex-direction: column; align-items: center; gap: 15px;">
            <div style="display: flex; gap: 20px; flex-wrap: wrap; justify-content: center;">
                <a href="privacy.html" style="color: #cbd5e1; text-decoration: none;">Privacy Policy</a>
                <a href="terms.html" style="color: #cbd5e1; text-decoration: none;">Terms of Service</a>
                <a href="shipping.html" style="color: #cbd5e1; text-decoration: none;">Shipping Policy</a>
                <a href="refund.html" style="color: #cbd5e1; text-decoration: none;">Refund Policy</a>
            </div>
            <p>&copy; 2026 Healthy Today Store Authorized Retailer. All Rights Reserved.</p>
            <p style="font-size: 0.75rem; color: #64748b; max-width: 800px; text-align: center; margin-top: 10px;">*These statements have not been evaluated by the Food and Drug Administration. These products are not intended to diagnose, treat, cure, or prevent any disease. Note: Clicking on a product will securely redirect you to the official manufacturer's page for final processing and fulfillment.</p>
        </div>
    </footer>
</body>
</html>
"""

shipping_content = """
    <h1>Shipping Policy</h1>
    <p>Thank you for visiting and shopping at Healthy Today Store. Following are the terms and conditions that constitute our Shipping Policy.</p>
    <h2>Domestic Shipping Policy</h2>
    <p><strong>Shipment processing time:</strong> All orders are processed within 1-2 business days. Orders are not shipped or delivered on weekends or holidays.</p>
    <p>If we are experiencing a high volume of orders, shipments may be delayed by a few days. Please allow additional days in transit for delivery. If there will be a significant delay in shipment of your order, we will contact you via email or telephone.</p>
    <h2>Shipping rates & delivery estimates</h2>
    <p>Shipping charges for your order will be calculated and displayed at checkout.</p>
    <ul>
        <li>Standard Shipping: 3-5 business days</li>
        <li>Expedited Shipping: 2-3 business days</li>
    </ul>
    <h2>International Shipping</h2>
    <p>We currently ship outside the U.S. to select countries. International shipping times vary between 7-14 business days depending on customs.</p>
"""

refund_content = """
    <h1>Refund & Return Policy</h1>
    <p>We stand behind our products and your satisfaction is our top priority.</p>
    <h2>Money-Back Guarantee</h2>
    <p>Most of our products are backed by a comprehensive money-back guarantee (ranging from 60 to 180 days, depending on the specific item). Please refer to the product page for exact guarantee terms.</p>
    <h2>Returns</h2>
    <p>To be eligible for a return, your item must be returned to the manufacturer's fulfillment center. To initiate a return, please contact our support team at support@healthytodaystore.com with your order number.</p>
    <h2>Refunds</h2>
    <p>Once your return is received and inspected, the manufacturer will send you an email to notify you that they have received your returned item. Your refund will be processed, and a credit will automatically be applied to your credit card or original method of payment, within a certain amount of days.</p>
    <h2>Contact Us</h2>
    <p>If you have any questions on how to return your item to us, contact us at support@healthytodaystore.com.</p>
"""

privacy_content = """
    <h1>Privacy Policy</h1>
    <p>Last updated: January 1, 2026</p>
    <p>At Healthy Today Store, we take your privacy seriously. This Privacy Policy describes how your personal information is collected, used, and shared when you visit or make a purchase from our store.</p>
    <h2>Personal Information We Collect</h2>
    <p>When you visit the Site, we automatically collect certain information about your device, including information about your web browser, IP address, time zone, and some of the cookies that are installed on your device.</p>
    <h2>How Do We Use Your Personal Information?</h2>
    <p>We use the Order Information that we collect generally to fulfill any orders placed through the Site (including processing your payment information, arranging for shipping, and providing you with invoices and/or order confirmations).</p>
    <h2>Changes</h2>
    <p>We may update this privacy policy from time to time in order to reflect, for example, changes to our practices or for other operational, legal or regulatory reasons.</p>
    <h2>Contact Us</h2>
    <p>For more information about our privacy practices, if you have questions, or if you would like to make a complaint, please contact us by e-mail at support@healthytodaystore.com.</p>
"""

terms_content = """
    <h1>Terms of Service</h1>
    <p>Last updated: January 1, 2026</p>
    <p>Welcome to Healthy Today Store. By accessing or using our website, you agree to be bound by these Terms of Service and all applicable laws and regulations.</p>
    <h2>Use License</h2>
    <p>Permission is granted to temporarily download one copy of the materials (information or software) on Healthy Today Store's website for personal, non-commercial transitory viewing only.</p>
    <h2>Disclaimer</h2>
    <p>The materials on Healthy Today Store's website are provided on an 'as is' basis. Healthy Today Store makes no warranties, expressed or implied, and hereby disclaims and negates all other warranties including, without limitation, implied warranties or conditions of merchantability, fitness for a particular purpose, or non-infringement of intellectual property or other violation of rights.</p>
    <h2>Limitations</h2>
    <p>In no event shall Healthy Today Store or its suppliers be liable for any damages (including, without limitation, damages for loss of data or profit, or due to business interruption) arising out of the use or inability to use the materials on Healthy Today Store's website.</p>
    <h2>Contact</h2>
    <p>Questions about the Terms of Service should be sent to us at support@healthytodaystore.com.</p>
"""

with open('loja/shipping.html', 'w', encoding='utf-8') as f:
    f.write(layout.replace('{TITLE}', 'Shipping Policy').replace('{CONTENT}', shipping_content))
    
with open('loja/refund.html', 'w', encoding='utf-8') as f:
    f.write(layout.replace('{TITLE}', 'Refund Policy').replace('{CONTENT}', refund_content))

with open('loja/privacy.html', 'w', encoding='utf-8') as f:
    f.write(layout.replace('{TITLE}', 'Privacy Policy').replace('{CONTENT}', privacy_content))

with open('loja/terms.html', 'w', encoding='utf-8') as f:
    f.write(layout.replace('{TITLE}', 'Terms of Service').replace('{CONTENT}', terms_content))
