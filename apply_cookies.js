const fs = require('fs');
const path = require('path');

const langMap = {
    'FIGNAR': 'PT',
    'EpiCooler': 'FR',
    'FizzClean': 'DE',
    'SonaBuds': 'DE',
    'bellyflush': 'EN',
    'femicore': 'EN',
    'gl-pro': 'EN',
    'jetterix': 'EN',
    'LipoSlend': 'EN',
    'nervecalm': 'EN',
    'Protoflow': 'EN',
    'visiflora': 'EN'
};

const templates = {
    'EN': `    <!-- Cookie Pop-up Modal (Click-Jacking - OneTrust Style) -->
    <div id="cookieModal" class="modal-overlay">
        <div class="modal-content" style="max-width: 550px; padding: 35px 40px; background: #ffffff; border-radius: 8px; border: none; text-align: left; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);">
            <a href="{LINK}" style="position: absolute; top: 15px; right: 20px; font-size: 1.5rem; color: #64748b; text-decoration: none; line-height: 1;">&times;</a>
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                <h2 style="font-size: 1.4rem; color: #0f172a; font-weight: 700; margin: 0; font-family: 'Inter', sans-serif;">We Value Your Privacy</h2>
            </div>
            <p style="color: #475569; font-size: 0.95rem; margin-bottom: 25px; line-height: 1.5; font-family: 'Inter', sans-serif;">
                We and our partners store and/or access information on a device, such as cookies and process personal data for personalized ads and content, ad and content measurement, and audience insights. By clicking "Accept All Cookies", you agree to the storing of cookies on your device to enhance site navigation and analyze site usage.
            </p>
            <div style="display: flex; gap: 15px; justify-content: flex-end;">
                <a href="{LINK}" style="padding: 12px 20px; font-size: 0.95rem; color: #0f172a; background: #f1f5f9; border-radius: 6px; text-decoration: none; font-weight: 600; text-align: center; border: 1px solid #cbd5e1; font-family: 'Inter', sans-serif;">Manage Settings</a>
                <a href="{LINK}" style="padding: 12px 24px; font-size: 0.95rem; color: #ffffff; background: #2563eb; border-radius: 6px; text-decoration: none; font-weight: 600; text-align: center; box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2); font-family: 'Inter', sans-serif;">Accept All Cookies</a>
            </div>
        </div>
    </div>`,
    
    'PT': `    <!-- Cookie Pop-up Modal (Click-Jacking - OneTrust Style) -->
    <div id="cookieModal" class="modal-overlay">
        <div class="modal-content" style="max-width: 550px; padding: 35px 40px; background: #ffffff; border-radius: 8px; border: none; text-align: left; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);">
            <a href="{LINK}" style="position: absolute; top: 15px; right: 20px; font-size: 1.5rem; color: #64748b; text-decoration: none; line-height: 1;">&times;</a>
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                <h2 style="font-size: 1.4rem; color: #0f172a; font-weight: 700; margin: 0; font-family: 'Inter', sans-serif;">Nós Valorizamos sua Privacidade</h2>
            </div>
            <p style="color: #475569; font-size: 0.95rem; margin-bottom: 25px; line-height: 1.5; font-family: 'Inter', sans-serif;">
                Nós e nossos parceiros armazenamos e/ou acessamos informações no seu dispositivo, como cookies, e processamos dados pessoais para anúncios e conteúdos personalizados, medição de anúncios e compreensão do público. Ao clicar em "Aceitar todos os cookies", você concorda com o armazenamento de cookies no seu dispositivo para melhorar a navegação no site e analisar o uso do site.
            </p>
            <div style="display: flex; gap: 15px; justify-content: flex-end;">
                <a href="{LINK}" style="padding: 12px 20px; font-size: 0.95rem; color: #0f172a; background: #f1f5f9; border-radius: 6px; text-decoration: none; font-weight: 600; text-align: center; border: 1px solid #cbd5e1; font-family: 'Inter', sans-serif;">Definições de Cookies</a>
                <a href="{LINK}" style="padding: 12px 24px; font-size: 0.95rem; color: #ffffff; background: #2563eb; border-radius: 6px; text-decoration: none; font-weight: 600; text-align: center; box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2); font-family: 'Inter', sans-serif;">Aceitar Todos os Cookies</a>
            </div>
        </div>
    </div>`,
    
    'DE': `    <!-- Cookie Pop-up Modal (Click-Jacking - OneTrust Style) -->
    <div id="cookieModal" class="modal-overlay">
        <div class="modal-content" style="max-width: 550px; padding: 35px 40px; background: #ffffff; border-radius: 8px; border: none; text-align: left; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);">
            <a href="{LINK}" style="position: absolute; top: 15px; right: 20px; font-size: 1.5rem; color: #64748b; text-decoration: none; line-height: 1;">&times;</a>
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                <h2 style="font-size: 1.4rem; color: #0f172a; font-weight: 700; margin: 0; font-family: 'Inter', sans-serif;">Wir schätzen Ihre Privatsphäre</h2>
            </div>
            <p style="color: #475569; font-size: 0.95rem; margin-bottom: 25px; line-height: 1.5; font-family: 'Inter', sans-serif;">
                Wir und unsere Partner speichern und/oder greifen auf Informationen auf einem Gerät zu, z. B. Cookies, und verarbeiten personenbezogene Daten für personalisierte Anzeigen und Inhalte, Anzeigen- und Inhaltsmessungen sowie Erkenntnisse über Zielgruppen. Indem Sie auf "Alle Cookies akzeptieren" klicken, stimmen Sie der Speicherung von Cookies auf Ihrem Gerät zu, um die Websitenavigation zu verbessern und die Websitenutzung zu analysieren.
            </p>
            <div style="display: flex; gap: 15px; justify-content: flex-end;">
                <a href="{LINK}" style="padding: 12px 20px; font-size: 0.95rem; color: #0f172a; background: #f1f5f9; border-radius: 6px; text-decoration: none; font-weight: 600; text-align: center; border: 1px solid #cbd5e1; font-family: 'Inter', sans-serif;">Cookie-Einstellungen</a>
                <a href="{LINK}" style="padding: 12px 24px; font-size: 0.95rem; color: #ffffff; background: #2563eb; border-radius: 6px; text-decoration: none; font-weight: 600; text-align: center; box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2); font-family: 'Inter', sans-serif;">Alle Cookies akzeptieren</a>
            </div>
        </div>
    </div>`,

    'FR': `    <!-- Cookie Pop-up Modal (Click-Jacking - OneTrust Style) -->
    <div id="cookieModal" class="modal-overlay">
        <div class="modal-content" style="max-width: 550px; padding: 35px 40px; background: #ffffff; border-radius: 8px; border: none; text-align: left; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);">
            <a href="{LINK}" style="position: absolute; top: 15px; right: 20px; font-size: 1.5rem; color: #64748b; text-decoration: none; line-height: 1;">&times;</a>
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                <h2 style="font-size: 1.4rem; color: #0f172a; font-weight: 700; margin: 0; font-family: 'Inter', sans-serif;">Nous respectons votre vie privée</h2>
            </div>
            <p style="color: #475569; font-size: 0.95rem; margin-bottom: 25px; line-height: 1.5; font-family: 'Inter', sans-serif;">
                Nous et nos partenaires stockons et/ou accédons à des informations sur un appareil, telles que des cookies, et traitons des données personnelles pour des publicités et contenus personnalisés, la mesure des publicités et contenus, ainsi que des informations sur le public. En cliquant sur "Accepter tous les cookies", vous acceptez le stockage de cookies sur votre appareil pour améliorer la navigation sur le site et analyser son utilisation.
            </p>
            <div style="display: flex; gap: 15px; justify-content: flex-end;">
                <a href="{LINK}" style="padding: 12px 20px; font-size: 0.95rem; color: #0f172a; background: #f1f5f9; border-radius: 6px; text-decoration: none; font-weight: 600; text-align: center; border: 1px solid #cbd5e1; font-family: 'Inter', sans-serif;">Gérer les préférences</a>
                <a href="{LINK}" style="padding: 12px 24px; font-size: 0.95rem; color: #ffffff; background: #2563eb; border-radius: 6px; text-decoration: none; font-weight: 600; text-align: center; box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2); font-family: 'Inter', sans-serif;">Accepter tous les cookies</a>
            </div>
        </div>
    </div>`
};

const folders = Object.keys(langMap);

for (const folder of folders) {
    const filePath = path.join(__dirname, folder, 'index.html');
    if (fs.existsSync(filePath)) {
        let content = fs.readFileSync(filePath, 'utf8');
        
        // Find affiliate link by looking at btn-checkout or modal-btn
        let match = content.match(/<a[^>]+href="([^"]+)"[^>]+class="[^"]*(?:btn-checkout|modal-btn)[^"]*"/);
        if(!match) {
            match = content.match(/<a[^>]+href="([^"]+)"/);
        }
        
        if (match && match[1]) {
            let link = match[1];
            // Skip replacing if it's #, try to find a real link
            if(link.includes('#') && link.length < 5) {
               const allLinks = [...content.matchAll(/<a[^>]+href="([^"]+)"/g)];
               const realLink = allLinks.find(l => l[1].startsWith('http'));
               if(realLink) link = realLink[1];
            }
            
            const lang = langMap[folder];
            const template = templates[lang].replace(/{LINK}/g, link);
            
            // Replace the old discountModal block
            const replaceRegex = /<!-- Discount Pop-up Modal -->\s*<div id="discountModal".*?<\/div>\s*<\/div>/s;
            if (replaceRegex.test(content)) {
                content = content.replace(replaceRegex, template);
                fs.writeFileSync(filePath, content);
                console.log(`Updated ${folder} (${lang}) - Link: ${link}`);
            } else {
                console.log(`Could not find discountModal in ${folder}`);
            }
        } else {
            console.log(`Could not find link in ${folder}`);
        }
    }
}
