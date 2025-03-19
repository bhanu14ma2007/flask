import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Enable CORS for frontend requests

# Initialize Flask app
app = Flask(__name__, template_folder="templates")
CORS(app)  # Allow frontend requests

search_data = [
    {"title": "Example Domain", "url": "https://example.com", "description": "This is an example website."},
    {"title": "Python Official", "url": "https://www.python.org", "description": "Python is a programming language."},
    {"title": "Flask Framework", "url": "https://flask.palletsprojects.com", "description": "Flask is a web framework for Python."},
    {"title": "valentine,s day surprise", "url": "https://bhanu14ma2007.github.io/very/", "description": "IT IS VAILITAYS DAY SEAPICIAL"},
    {"title": "Amazon ", "url": "https://www.amazon.com/", "description": "amazon is shopping website that shows more thing that in online"}, 
    {
    "title": "Apple",
    "url": "https://www.apple.com",
    "description": "Official site for Apple products such as iPhones, MacBooks, iPads, and software services."
  },
  {
    "title": "Adobe",
    "url": "https://www.adobe.com",
    "description": "Provides creative software like Photoshop, Illustrator, and Acrobat for design and document management."
  },
  {
    "title": "Airbnb",
    "url": "https://www.airbnb.com",
    "description": "A platform to book unique accommodations and experiences worldwide."
  },
  {
    "title": "Alibaba",
    "url": "https://www.alibaba.com",
    "description": "A global wholesale marketplace connecting buyers and suppliers."
  },
  {
    "title": "AOL",
    "url": "https://www.aol.com",
    "description": "A web portal offering email, news, entertainment, and more."
  },
  {
    "title": "Ask",
    "url": "https://www.ask.com",
    "description": "A question-and-answer-based search engine for finding information."
  },
  {
    "title": "AccuWeather",
    "url": "https://www.accuweather.com",
    "description": "Provides real-time weather forecasts and climate updates globally."
  },
  {
    "title": "Aetna",
    "url": "https://www.aetna.com",
    "description": "A health insurance provider offering various plans and services."
  },
  {
    "title": "Ancestry",
    "url": "https://www.ancestry.com",
    "description": "A genealogy platform to explore family history and DNA testing."
  },
   {
    "title": "BBC",
    "url": "https://www.bbc.com",
    "description": "A global news organization providing the latest news, analysis, and documentaries."
  },
  {
    "title": "Bing",
    "url": "https://www.bing.com",
    "description": "A search engine by Microsoft that provides web, image, and video search."
  },
  {
    "title": "Best Buy",
    "url": "https://www.bestbuy.com",
    "description": "A retailer specializing in electronics, appliances, and gadgets."
  },
  {
    "title": "Bank of America",
    "url": "https://www.bankofamerica.com",
    "description": "One of the largest banking institutions offering financial services worldwide."
  },
  {
    "title": "Bloomberg",
    "url": "https://www.bloomberg.com",
    "description": "A global financial and business news platform providing real-time data."
  },
  {
    "title": "BuzzFeed",
    "url": "https://www.buzzfeed.com",
    "description": "A digital media company known for viral news, entertainment, and quizzes."
  },
  {
    "title": "Business Insider",
    "url": "https://www.businessinsider.com",
    "description": "A financial and business news website covering markets, tech, and industry trends."
  },
  {
    "title": "Booking.com",
    "url": "https://www.booking.com",
    "description": "A travel website for booking hotels, flights, and vacation rentals."
  },
  {
    "title": "Baidu",
    "url": "https://www.baidu.com",
    "description": "China’s largest search engine, similar to Google, providing search and AI services."
  },
  {
    "title": "Box",
    "url": "https://www.box.com",
    "description": "A cloud storage and file-sharing service for businesses and individuals."
  },
  {
    "title": "CNN",
    "url": "https://www.cnn.com",
    "description": "A global news network providing the latest breaking news, politics, and analysis."
  },
  {
    "title": "Craigslist",
    "url": "https://www.craigslist.org",
    "description": "An online classifieds platform for jobs, housing, services, and more."
  },
  {
    "title": "Cisco",
    "url": "https://www.cisco.com",
    "description": "A technology company specializing in networking, cybersecurity, and IT solutions."
  },
  {
    "title": "CBS",
    "url": "https://www.cbs.com",
    "description": "A major television network offering news, entertainment, and sports."
  },
  {
    "title": "Capital One",
    "url": "https://www.capitalone.com",
    "description": "A banking and financial services company offering credit cards, loans, and accounts."
  },
  {
    "title": "CNET",
    "url": "https://www.cnet.com",
    "description": "A technology news and reviews site covering gadgets, software, and industry trends."
  },
  {
    "title": "Cloudflare",
    "url": "https://www.cloudflare.com",
    "description": "A web security and performance company providing CDN and DDoS protection services."
  },
  {
    "title": "Canva",
    "url": "https://www.canva.com",
    "description": "An online design tool for creating graphics, presentations, and social media posts."
  },
  {
    "title": "Coursera",
    "url": "https://www.coursera.org",
    "description": "An online learning platform offering courses from top universities and institutions."
  },
  {
    "title": "Codeacademy",
    "url": "https://www.codecademy.com",
    "description": "An interactive learning platform for coding and programming skills."
  },
   {
    "title": "Dropbox",
    "url": "https://www.dropbox.com",
    "description": "A cloud storage service for file sharing and collaboration."
  },
  {
    "title": "Disney",
    "url": "https://www.disney.com",
    "description": "The official website for Disney movies, TV shows, theme parks, and more."
  },
  {
    "title": "eBay",
    "url": "https://www.ebay.com",
    "description": "An online marketplace for buying and selling goods through auctions and direct sales."
  },
  {
    "title": "ESPN",
    "url": "https://www.espn.com",
    "description": "A leading sports news and streaming service covering global sports events."
  },
  {
    "title": "Facebook",
    "url": "https://www.facebook.com",
    "description": "A social media platform for connecting with friends and sharing content."
  },
  {
    "title": "Forbes",
    "url": "https://www.forbes.com",
    "description": "A business and finance news site covering markets, entrepreneurs, and technology."
  },
  {
    "title": "Google",
    "url": "https://www.google.com",
    "description": "The world's leading search engine and provider of online services like Gmail and Maps."
  },
  {
    "title": "GitHub",
    "url": "https://www.github.com",
    "description": "A platform for hosting and collaborating on software development projects."
  },
  {
    "title": "Hulu",
    "url": "https://www.hulu.com",
    "description": "A streaming service offering TV shows, movies, and original content."
  },
  {
    "title": "HP",
    "url": "https://www.hp.com",
    "description": "A technology company known for computers, printers, and IT services."
  },
  {
    "title": "Instagram",
    "url": "https://www.instagram.com",
    "description": "A social media platform for sharing photos, videos, and stories."
  },
  {
    "title": "Intel",
    "url": "https://www.intel.com",
    "description": "A leading semiconductor company specializing in processors and computing technology."
  },
  {
    "title": "JPMorgan Chase",
    "url": "https://www.jpmorganchase.com",
    "description": "A global banking and financial services provider."
  },
  {
    "title": "JetBrains",
    "url": "https://www.jetbrains.com",
    "description": "A software company providing IDEs and development tools."
  },
  {
    "title": "Kickstarter",
    "url": "https://www.kickstarter.com",
    "description": "A crowdfunding platform for creative projects and innovations."
  },
  {
    "title": "Khan Academy",
    "url": "https://www.khanacademy.org",
    "description": "A free online education platform offering courses in various subjects."
  },
  {
    "title": "LinkedIn",
    "url": "https://www.linkedin.com",
    "description": "A professional networking platform for job seekers and businesses."
  },
  {
    "title": "Linux",
    "url": "https://www.linux.org",
    "description": "A site dedicated to the open-source Linux operating system."
  },
  {
    "title": "Microsoft",
    "url": "https://www.microsoft.com",
    "description": "A technology company known for Windows, Office, and cloud services."
  },
  {
    "title": "Medium",
    "url": "https://www.medium.com",
    "description": "A blogging and publishing platform for writers and readers."
  },
  {
    "title": "Netflix",
    "url": "https://www.netflix.com",
    "description": "A popular streaming service offering movies, TV shows, and original content."
  },
  {
    "title": "NASA",
    "url": "https://www.nasa.gov",
    "description": "The official website of the U.S. space agency, providing space exploration news and research."
  },
  {
    "title": "Opera",
    "url": "https://www.opera.com",
    "description": "A web browser company offering fast and secure browsing solutions."
  },
  {
    "title": "Oracle",
    "url": "https://www.oracle.com",
    "description": "A leading provider of database and cloud computing solutions."
  },
  {
    "title": "PayPal",
    "url": "https://www.paypal.com",
    "description": "An online payment service for secure transactions and money transfers."
  },
  {
    "title": "Pinterest",
    "url": "https://www.pinterest.com",
    "description": "A social media platform for discovering and sharing creative ideas."
  },
  {
    "title": "Quora",
    "url": "https://www.quora.com",
    "description": "A question-and-answer platform where users share knowledge and expertise."
  },
  {
    "title": "QuickBooks",
    "url": "https://www.quickbooks.intuit.com",
    "description": "An accounting software solution for businesses and freelancers."
  },
  {
    "title": "Reddit",
    "url": "https://www.reddit.com",
    "description": "A discussion platform with user-generated content on various topics."
  },
  {
    "title": "Reuters",
    "url": "https://www.reuters.com",
    "description": "An international news agency covering business, politics, and global affairs."
  },
  {
    "title": "Spotify",
    "url": "https://www.spotify.com",
    "description": "A music streaming service offering millions of songs and podcasts."
  },
  {
    "title": "Salesforce",
    "url": "https://www.salesforce.com",
    "description": "A cloud-based CRM platform for businesses and customer management."
  },
  {
    "title": "Twitter",
    "url": "https://www.twitter.com",
    "description": "A social media platform for short-form content and real-time news updates."
  },
  {
    "title": "Tesla",
    "url": "https://www.tesla.com",
    "description": "An electric vehicle and clean energy company founded by Elon Musk."
  },
  {
    "title": "Uber",
    "url": "https://www.uber.com",
    "description": "A ride-sharing and food delivery platform operating worldwide."
  },
  {
    "title": "Udemy",
    "url": "https://www.udemy.com",
    "description": "An online learning marketplace with courses on various topics."
  },
  {
    "title": "Verizon",
    "url": "https://www.verizon.com",
    "description": "A telecommunications company providing mobile and internet services."
  },
  {
    "title": "Vimeo",
    "url": "https://www.vimeo.com",
    "description": "A video-sharing platform focused on high-quality content for creators."
  },
  {
    "title": "Wikipedia",
    "url": "https://www.wikipedia.org",
    "description": "A free, collaboratively edited online encyclopedia with millions of articles."
  },
  {
    "title": "Walmart",
    "url": "https://www.walmart.com",
    "description": "A multinational retail corporation operating hypermarkets and e-commerce stores."
  },
  {
    "title": "Xbox",
    "url": "https://www.xbox.com",
    "description": "The official website for Microsoft's gaming console and services."
  },
  {
    "title": "Xfinity",
    "url": "https://www.xfinity.com",
    "description": "A telecommunications service provider offering internet, TV, and phone services."
  },
  {
    "title": "YouTube",
    "url": "https://www.youtube.com",
    "description": "A video-sharing platform for content creators, music, and entertainment."
  },
  {
    "title": "Yahoo",
    "url": "https://www.yahoo.com",
    "description": "A web portal offering news, email, search, and finance services."
  },
  {
    "title": "Zillow",
    "url": "https://www.zillow.com",
    "description": "A real estate marketplace for buying, selling, and renting properties."
  },
  {
    "title": "Zoom",
    "url": "https://www.zoom.us",
    "description": "A video conferencing platform used for meetings, webinars, and virtual events."
  },
  {
    "title": "Dell",
    "url": "https://www.dell.com",
    "description": "A multinational computer technology company that develops, sells, and supports computers and related products."
  },
  {
    "title": "Dailymotion",
    "url": "https://www.dailymotion.com",
    "description": "A video-sharing platform that allows users to upload, view, and share videos."
  },
  {
    "title": "Evernote",
    "url": "https://www.evernote.com",
    "description": "A note-taking and organization app for storing and managing information."
  },
  {
    "title": "Expedia",
    "url": "https://www.expedia.com",
    "description": "An online travel booking website for flights, hotels, and vacation packages."
  },
  {
    "title": "Fiverr",
    "url": "https://www.fiverr.com",
    "description": "A global online marketplace for freelance services in various industries."
  },
  {
    "title": "Flipkart",
    "url": "https://www.flipkart.com",
    "description": "A leading Indian e-commerce website for online shopping of electronics, fashion, and more."
  },
  {
    "title": "Glassdoor",
    "url": "https://www.glassdoor.com",
    "description": "A website for job listings, company reviews, and salary insights."
  },
  {
    "title": "GoDaddy",
    "url": "https://www.godaddy.com",
    "description": "A domain registrar and web hosting company for individuals and businesses."
  },
  {
    "title": "Hotels.com",
    "url": "https://www.hotels.com",
    "description": "An online hotel booking service for accommodations worldwide."
  },
  {
    "title": "HostGator",
    "url": "https://www.hostgator.com",
    "description": "A web hosting company providing hosting and domain registration services."
  },
  {
    "title": "Indeed",
    "url": "https://www.indeed.com",
    "description": "A job search engine that aggregates job listings from various sources."
  },
  {
    "title": "Imgur",
    "url": "https://www.imgur.com",
    "description": "An online image-sharing and meme-creation platform."
  },
  {
    "title": "Jotform",
    "url": "https://www.jotform.com",
    "description": "An online tool for creating and managing web forms."
  },
  {
    "title": "Joomla",
    "url": "https://www.joomla.org",
    "description": "An open-source content management system for building websites."
  },
  {
    "title": "Kickstarter",
    "url": "https://www.kickstarter.com",
    "description": "A crowdfunding platform for creative projects and innovations."
  },
  {
    "title": "Kaspersky",
    "url": "https://www.kaspersky.com",
    "description": "A cybersecurity company offering antivirus and online protection software."
  },
  {
    "title": "Lynda",
    "url": "https://www.lynda.com",
    "description": "An online learning platform offering courses in business, technology, and design."
  },
  {
    "title": "Lumen",
    "url": "https://www.lumen.com",
    "description": "A technology company providing networking and cloud services."
  },
  {
    "title": "Zynga",
    "url": "https://www.zynga.com",
    "description": "A game development company known for social and mobile games."
  },
  {
    "title": "Zoho",
    "url": "https://www.zoho.com",
    "description": "A suite of online productivity and business software solutions."
  },
  {
    "title": "Discord",
    "url": "https://www.discord.com",
    "description": "A communication platform for voice, video, and text chat, popular among gaming communities."
  },
  {
    "title": "DuckDuckGo",
    "url": "https://www.duckduckgo.com",
    "description": "A privacy-focused search engine that does not track users."
  },
  {
    "title": "Duolingo",
    "url": "https://www.duolingo.com",
    "description": "A language-learning platform that offers free courses in multiple languages."
  },
  {
    "title": "Etsy",
    "url": "https://www.etsy.com",
    "description": "An online marketplace for handmade, vintage, and unique goods."
  },
  {
    "title": "EverWeb",
    "url": "https://www.everweb.com",
    "description": "A website-building tool for macOS users."
  },
  {
    "title": "Fandom",
    "url": "https://www.fandom.com",
    "description": "A website hosting fan-created content about movies, games, and TV shows."
  },
  {
    "title": "Fox News",
    "url": "https://www.foxnews.com",
    "description": "A major news website covering politics, world events, and entertainment."
  },
  {
    "title": "GOG",
    "url": "https://www.gog.com",
    "description": "A digital distribution platform for DRM-free video games."
  },
  {
    "title": "Grammarly",
    "url": "https://www.grammarly.com",
    "description": "An AI-powered writing assistant for improving grammar and style."
  },
  {
    "title": "HubSpot",
    "url": "https://www.hubspot.com",
    "description": "A customer relationship management (CRM) and marketing software platform."
  },
  {
    "title": "HackerRank",
    "url": "https://www.hackerrank.com",
    "description": "A coding practice platform for developers and technical recruiters."
  },
  {
    "title": "IEEE",
    "url": "https://www.ieee.org",
    "description": "A professional organization for engineers and technology professionals."
  },
  {
    "title": "Imgflip",
    "url": "https://www.imgflip.com",
    "description": "A website for creating and sharing memes and GIFs."
  },
  {
    "title": "JustWatch",
    "url": "https://www.justwatch.com",
    "description": "A streaming guide that helps users find where to watch movies and TV shows online."
  },
  {
    "title": "Jango",
    "url": "https://www.jango.com",
    "description": "A free music streaming service with personalized radio stations."
  },
  {
    "title": "Kayak",
    "url": "https://www.kayak.com",
    "description": "A travel search engine for flights, hotels, and car rentals."
  },
  {
    "title": "Komodo IDE",
    "url": "https://www.activestate.com/products/komodo-ide/",
    "description": "An integrated development environment (IDE) for programming and software development."
  },
  {
    "title": "LiveScience",
    "url": "https://www.livescience.com",
    "description": "A science news website covering discoveries, space, and health topics."
  },
  {
    "title": "Lotto247",
    "url": "https://www.lotto247.com",
    "description": "An online lottery platform offering international lottery tickets."
  },
  {
    "title": "Mozilla",
    "url": "https://www.mozilla.org",
    "description": "The organization behind the Firefox web browser and open-source web technologies."
  },
  {
    "title": "Mashable",
    "url": "https://www.mashable.com",
    "description": "A digital media website covering tech, entertainment, and culture news."
  },
  {
    "title": "Newegg",
    "url": "https://www.newegg.com",
    "description": "An online retailer specializing in computer hardware and electronics."
  },
  {
    "title": "NASA",
    "url": "https://www.nasa.gov",
    "description": "The official website of the National Aeronautics and Space Administration (NASA)."
  },
  {
    "title": "Quora",
    "url": "https://www.quora.com",
    "description": "A question-and-answer website where users share knowledge on various topics."
  },
  {
    "title": "Zapier",
    "url": "https://www.zapier.com",
    "description": "An automation tool that connects apps and automates workflows."
  },
  {
    "title": "DataCamp",
    "url": "https://www.datacamp.com",
    "description": "An online platform for learning data science and analytics."
  },
  {
    "title": "DigitalOcean",
    "url": "https://www.digitalocean.com",
    "description": "A cloud computing provider for developers and businesses."
  },
  {
    "title": "Dev.to",
    "url": "https://www.dev.to",
    "description": "A community-driven blogging platform for software developers."
  },
  {
    "title": "Engadget",
    "url": "https://www.engadget.com",
    "description": "A technology blog covering gadgets, consumer electronics, and tech news."
  },
  {
    "title": "Eclipse",
    "url": "https://www.eclipse.org",
    "description": "An open-source software development platform and IDE."
  },
  {
    "title": "Envato",
    "url": "https://www.envato.com",
    "description": "A marketplace for digital assets, templates, and creative tools."
  },
  {
    "title": "Fastly",
    "url": "https://www.fastly.com",
    "description": "A content delivery network (CDN) that accelerates websites and APIs."
  },
  {
    "title": "Fossbytes",
    "url": "https://www.fossbytes.com",
    "description": "A website covering open-source software, cybersecurity, and tech news."
  },
  {
    "title": "GameSpot",
    "url": "https://www.gamespot.com",
    "description": "A gaming website with news, reviews, and industry coverage."
  },
  {
    "title": "Giphy",
    "url": "https://www.giphy.com",
    "description": "A search engine for animated GIFs and stickers."
  },
  {
    "title": "Humble Bundle",
    "url": "https://www.humblebundle.com",
    "description": "A platform that sells games, books, and software bundles for charity."
  },
  {
    "title": "HackerOne",
    "url": "https://www.hackerone.com",
    "description": "A bug bounty platform that connects ethical hackers with companies."
  },
  {
    "title": "iFixit",
    "url": "https://www.ifixit.com",
    "description": "A website that provides repair guides and tools for fixing devices."
  },
  {
    "title": "Infosec Institute",
    "url": "https://www.infosecinstitute.com",
    "description": "A cybersecurity training provider offering courses and certifications."
  },
  {
    "title": "Jitsi",
    "url": "https://www.jitsi.org",
    "description": "An open-source video conferencing platform."
  },
  {
    "title": "Jupyter",
    "url": "https://www.jupyter.org",
    "description": "An open-source project providing interactive computing notebooks."
  },
  {
    "title": "Kickass Torrents",
    "url": "https://www.kickasstorrents.to",
    "description": "A torrent site for peer-to-peer file sharing."
  },
  {
    "title": "Khan Academy",
    "url": "https://www.khanacademy.org",
    "description": "A free educational platform offering courses in various subjects."
  },
  {
    "title": "LibreOffice",
    "url": "https://www.libreoffice.org",
    "description": "An open-source office suite for document editing and productivity."
  },
  {
    "title": "Lichess",
    "url": "https://www.lichess.org",
    "description": "A free online chess platform with various game modes."
  },
  {
    "title": "Mendeley",
    "url": "https://www.mendeley.com",
    "description": "A reference manager and research collaboration tool."
  },
  {
    "title": "Mixcloud",
    "url": "https://www.mixcloud.com",
    "description": "A streaming platform for DJs, radio shows, and podcasts."
  },
  {
    "title": "Ninite",
    "url": "https://www.ninite.com",
    "description": "A tool for installing and updating multiple applications at once."
  },
  {
    "title": "Namecheap",
    "url": "https://www.namecheap.com",
    "description": "A domain registrar and web hosting service."
  },
  {
    "title": "Odysee",
    "url": "https://www.odysee.com",
    "description": "A decentralized video-sharing platform using blockchain technology."
  },
  {
    "title": "Opera",
    "url": "https://www.opera.com",
    "description": "A web browser with built-in privacy features and a free VPN."
  },
  {
    "title": "Pexels",
    "url": "https://www.pexels.com",
    "description": "A free stock photo and video website."
  },
  {
    "title": "ProtonMail",
    "url": "https://www.protonmail.com",
    "description": "An encrypted email service focused on privacy and security."
  },
  {
    "title": "Qwant",
    "url": "https://www.qwant.com",
    "description": "A privacy-focused search engine based in France."
  },
  {
    "title": "Qt Project",
    "url": "https://www.qt.io",
    "description": "An open-source framework for developing cross-platform applications."
  },
  {
    "title": "Raspberry Pi",
    "url": "https://www.raspberrypi.org",
    "description": "The official website for Raspberry Pi, a small single-board computer."
  },
  {
    "title": "RapidAPI",
    "url": "https://www.rapidapi.com",
    "description": "A marketplace for APIs, providing integration solutions for developers."
  },
  {
    "title": "SourceForge",
    "url": "https://www.sourceforge.net",
    "description": "A platform for hosting and sharing open-source software projects."
  },
  {
    "title": "Stack Exchange",
    "url": "https://www.stackexchange.com",
    "description": "A network of Q&A sites for different topics, including programming."
  },
  {
    "title": "Trello",
    "url": "https://www.trello.com",
    "description": "A visual project management tool for organizing tasks and workflows."
  },
  {
    "title": "TechCrunch",
    "url": "https://www.techcrunch.com",
    "description": "A technology news website covering startups and industry trends."
  },
  {
    "title": "Ubuntu",
    "url": "https://www.ubuntu.com",
    "description": "The official website for the Ubuntu operating system."
  },
  {
    "title": "Udemy",
    "url": "https://www.udemy.com",
    "description": "An online learning platform offering courses in various subjects."
  },
  {
    "title": "Vivaldi",
    "url": "https://www.vivaldi.com",
    "description": "A web browser with advanced customization options."
  },
  {
    "title": "Vimeo",
    "url": "https://www.vimeo.com",
    "description": "A video-sharing platform for high-quality and creative content."
  },
  {
    "title": "Wire",
    "url": "https://www.wire.com",
    "description": "A secure messaging app focused on privacy and encryption."
  },
  {
    "title": "Wikihow",
    "url": "https://www.wikihow.com",
    "description": "A website with step-by-step guides on various topics."
  },
  {
    "title": "XDA Developers",
    "url": "https://www.xda-developers.com",
    "description": "A community for developers and technology enthusiasts."
  },
  {
    "title": "Y Combinator",
    "url": "https://www.ycombinator.com",
    "description": "A startup accelerator that helps early-stage companies grow."
  },
  {
    "title": "Zillow",
    "url": "https://www.zillow.com",
    "description": "A real estate marketplace for buying, selling, and renting homes."
  },
  {
    "title": "Digital Trends",
    "url": "https://www.digitaltrends.com",
    "description": "A technology news and review website covering gadgets, software, and emerging trends."
  },
  {
    "title": "Datawrapper",
    "url": "https://www.datawrapper.de",
    "description": "A tool that helps users create charts, maps, and tables for data visualization."
  },
  {
    "title": "DevDocs",
    "url": "https://devdocs.io",
    "description": "A fast, offline-friendly documentation browser for developers."
  },
  {
    "title": "DeepL",
    "url": "https://www.deepl.com",
    "description": "An advanced AI-powered translation service."
  },
  {
    "title": "Dribbble",
    "url": "https://dribbble.com",
    "description": "A community for designers to showcase their work and connect with potential clients."
  },
  {
    "title": "EarthSky",
    "url": "https://earthsky.org",
    "description": "A website providing daily updates on astronomy and space-related news."
  },
  {
    "title": "Elasticsearch",
    "url": "https://www.elastic.co",
    "description": "A powerful search and analytics engine for businesses and developers."
  },
  {
    "title": "Etsy",
    "url": "https://www.etsy.com",
    "description": "An e-commerce marketplace for handmade and vintage goods."
  },
  {
    "title": "Epic Games",
    "url": "https://www.epicgames.com",
    "description": "A video game company known for Fortnite and the Unreal Engine."
  },
  {
    "title": "Evernote",
    "url": "https://www.evernote.com",
    "description": "A note-taking app that helps users capture and organize their ideas."
  },
  {
    "title": "Fandom",
    "url": "https://www.fandom.com",
    "description": "A platform for fan-created wikis about movies, TV shows, and games."
  },
  {
    "title": "Fiverr",
    "url": "https://www.fiverr.com",
    "description": "A freelance services marketplace for various digital skills."
  },
  {
    "title": "Flipboard",
    "url": "https://www.flipboard.com",
    "description": "A news aggregation and content curation platform."
  },
  {
    "title": "Freelancer",
    "url": "https://www.freelancer.com",
    "description": "A global freelancing marketplace connecting businesses with professionals."
  },
  {
    "title": "GitLab",
    "url": "https://gitlab.com",
    "description": "A web-based DevOps lifecycle tool providing source code management."
  },
  {
    "title": "GOG",
    "url": "https://www.gog.com",
    "description": "A DRM-free video game distribution platform."
  },
  {
    "title": "Gutenberg Project",
    "url": "https://www.gutenberg.org",
    "description": "A library of free eBooks, including classics in the public domain."
  },
  {
    "title": "HackerRank",
    "url": "https://www.hackerrank.com",
    "description": "A platform that helps developers improve coding skills through challenges."
  },
  {
    "title": "Hashnode",
    "url": "https://hashnode.com",
    "description": "A blogging platform for developers to share knowledge and insights."
  },
  {
    "title": "Heroku",
    "url": "https://www.heroku.com",
    "description": "A cloud platform for deploying, managing, and scaling applications."
  },
  {
    "title": "Icons8",
    "url": "https://icons8.com",
    "description": "A resource for free icons, illustrations, and design assets."
  },
  {
    "title": "Imgur",
    "url": "https://imgur.com",
    "description": "A popular image-sharing website known for memes and viral content."
  },
  {
    "title": "Indeed",
    "url": "https://www.indeed.com",
    "description": "A job search website with listings from around the world."
  },
  {
    "title": "Jira",
    "url": "https://www.atlassian.com/software/jira",
    "description": "A project management tool for agile development teams."
  },
  {
    "title": "JustWatch",
    "url": "https://www.justwatch.com",
    "description": "A streaming guide that helps users find where to watch movies and TV shows."
  },
  {
    "title": "Kaggle",
    "url": "https://www.kaggle.com",
    "description": "A platform for data science competitions and learning resources."
  },
  {
    "title": "KeyCDN",
    "url": "https://www.keycdn.com",
    "description": "A content delivery network (CDN) optimizing website speed."
  },
  {
    "title": "Last.fm",
    "url": "https://www.last.fm",
    "description": "A music tracking and recommendation service."
  },
  {
    "title": "LottieFiles",
    "url": "https://lottiefiles.com",
    "description": "A platform for sharing and discovering animation files."
  },
  {
    "title": "Medium",
    "url": "https://medium.com",
    "description": "A blogging platform where writers share stories and ideas."
  },
  {
    "title": "Mozilla",
    "url": "https://www.mozilla.org",
    "description": "The non-profit behind Firefox and other internet privacy projects."
  },
  {
    "title": "Notion",
    "url": "https://www.notion.so",
    "description": "An all-in-one workspace for notes, tasks, and collaboration."
  },
  {
    "title": "NPR",
    "url": "https://www.npr.org",
    "description": "A public radio network providing news, podcasts, and culture stories."
  },
  {
    "title": "Oculus",
    "url": "https://www.oculus.com",
    "description": "A virtual reality company owned by Meta."
  },
  {
    "title": "OpenAI",
    "url": "https://www.openai.com",
    "description": "An artificial intelligence research organization."
  },
  {
    "title": "Pixabay",
    "url": "https://www.pixabay.com",
    "description": "A platform offering free stock photos and videos."
  },
  {
    "title": "Quora",
    "url": "https://www.quora.com",
    "description": "A question-and-answer website where users share knowledge."
  },
  {
    "title": "Reddit",
    "url": "https://www.reddit.com",
    "description": "A social platform with communities for various interests."
  },
  {
    "title": "Replit",
    "url": "https://replit.com",
    "description": "An online IDE for coding and collaboration."
  },
  {
    "title": "Shodan",
    "url": "https://www.shodan.io",
    "description": "A search engine for internet-connected devices."
  },
  {
    "title": "Stack Overflow",
    "url": "https://stackoverflow.com",
    "description": "A Q&A site for programmers."
  },
  {
    "title": "Twitch",
    "url": "https://www.twitch.tv",
    "description": "A live streaming platform primarily for gamers."
  },
  {
    "title": "Udacity",
    "url": "https://www.udacity.com",
    "description": "An online education platform offering technology courses."
  },
  {
    "title": "Wired",
    "url": "https://www.wired.com",
    "description": "A tech magazine covering science, business, and innovation."
  },
  {
    "title": "Zapier",
    "url": "https://zapier.com",
    "description": "A workflow automation tool connecting apps and services."
  },
  {
    "title": "Digital Foundry",
    "url": "https://www.eurogamer.net/digitalfoundry",
    "description": "A tech analysis site specializing in gaming hardware and performance."
  },
  {
    "title": "DTube",
    "url": "https://d.tube",
    "description": "A decentralized video-sharing platform using blockchain technology."
  },
  {
    "title": "Dev.to",
    "url": "https://dev.to",
    "description": "A community-driven platform for developers to share insights and tutorials."
  },
  {
    "title": "DataCamp",
    "url": "https://www.datacamp.com",
    "description": "An interactive learning platform for data science and analytics."
  },
  {
    "title": "DxOMark",
    "url": "https://www.dxomark.com",
    "description": "A site that reviews and ranks cameras, smartphones, and audio devices."
  },
  {
    "title": "Expensify",
    "url": "https://www.expensify.com",
    "description": "A tool that helps businesses track and manage expenses efficiently."
  },
  {
    "title": "Envato Elements",
    "url": "https://elements.envato.com",
    "description": "A resource for royalty-free assets including templates, music, and graphics."
  },
  {
    "title": "Engadget",
    "url": "https://www.engadget.com",
    "description": "A tech media site offering news and reviews on gadgets and software."
  },
  {
    "title": "Eventbrite",
    "url": "https://www.eventbrite.com",
    "description": "A platform for discovering and managing events worldwide."
  },
  {
    "title": "EverWeb",
    "url": "https://www.everwebapp.com",
    "description": "A website builder designed for macOS users."
  },
  {
    "title": "Feedly",
    "url": "https://www.feedly.com",
    "description": "A news aggregator and RSS feed reader for organizing web content."
  },
  {
    "title": "Framer",
    "url": "https://www.framer.com",
    "description": "A prototyping tool for designers and developers."
  },
  {
    "title": "FastAPI",
    "url": "https://fastapi.tiangolo.com",
    "description": "A high-performance web framework for building APIs with Python."
  },
  {
    "title": "Flowbite",
    "url": "https://flowbite.com",
    "description": "A UI component library based on Tailwind CSS."
  },
  {
    "title": "Ghost",
    "url": "https://ghost.org",
    "description": "A powerful open-source platform for modern publishing."
  },
  {
    "title": "Glitch",
    "url": "https://glitch.com",
    "description": "A coding platform for building and remixing web applications."
  },
  {
    "title": "GeoGuessr",
    "url": "https://www.geoguessr.com",
    "description": "An online game that challenges players to guess locations on Google Maps."
  },
  {
    "title": "GraphQL",
    "url": "https://graphql.org",
    "description": "A query language and runtime for APIs, designed to improve flexibility and efficiency."
  },
  {
    "title": "Hotjar",
    "url": "https://www.hotjar.com",
    "description": "A website analytics tool that provides heatmaps, session recordings, and user feedback."
  },
  {
    "title": "Houdini",
    "url": "https://houdini.org",
    "description": "A powerful software suite for 3D animation and visual effects."
  },
  {
    "title": "Hemingway Editor",
    "url": "https://hemingwayapp.com",
    "description": "An online tool that helps writers improve readability and style."
  },
  {
    "title": "Investopedia",
    "url": "https://www.investopedia.com",
    "description": "A financial education website offering insights on investing and personal finance."
  },
  {
    "title": "Iconfinder",
    "url": "https://www.iconfinder.com",
    "description": "A marketplace for free and premium vector icons."
  },
  {
    "title": "ImgBB",
    "url": "https://imgbb.com",
    "description": "A free image hosting and sharing platform."
  },
  {
    "title": "Inkscape",
    "url": "https://inkscape.org",
    "description": "A free and open-source vector graphics editor."
  },
  {
    "title": "Jitsi Meet",
    "url": "https://meet.jit.si",
    "description": "An open-source video conferencing solution with end-to-end encryption."
  },
  {
    "title": "JSFiddle",
    "url": "https://jsfiddle.net",
    "description": "An online editor for testing and sharing JavaScript, HTML, and CSS code."
  },
  {
    "title": "Joplin",
    "url": "https://joplinapp.org",
    "description": "A free, open-source note-taking and to-do application."
  },
  {
    "title": "Keybr",
    "url": "https://www.keybr.com",
    "description": "An online typing tutor designed to improve speed and accuracy."
  },
  {
    "title": "Krita",
    "url": "https://krita.org",
    "description": "A professional open-source painting program designed for artists."
  },
  {
    "title": "Lichess",
    "url": "https://lichess.org",
    "description": "A free online chess platform with puzzles, tournaments, and AI opponents."
  },
  {
    "title": "LibreOffice",
    "url": "https://www.libreoffice.org",
    "description": "A free and open-source office suite for document editing and productivity."
  },
  {
    "title": "Miro",
    "url": "https://miro.com",
    "description": "A collaborative online whiteboard platform for teams."
  },
  {
    "title": "Mastodon",
    "url": "https://mastodon.social",
    "description": "A decentralized social networking platform."
  },
  {
    "title": "Mixcloud",
    "url": "https://www.mixcloud.com",
    "description": "A platform for DJs and radio shows to stream their content."
  },
  {
    "title": "Namecheap",
    "url": "https://www.namecheap.com",
    "description": "A domain registration and web hosting service."
  },
  {
    "title": "Neocities",
    "url": "https://neocities.org",
    "description": "A free website hosting service focused on personal and creative sites."
  },
  {
    "title": "Observable",
    "url": "https://observablehq.com",
    "description": "A web-based platform for exploring and visualizing data."
  },
  {
    "title": "Otter.ai",
    "url": "https://otter.ai",
    "description": "An AI-powered transcription and note-taking tool."
  },
  {
    "title": "Pexels",
    "url": "https://www.pexels.com",
    "description": "A website offering free stock photos and videos."
  },
  {
    "title": "RunKit",
    "url": "https://runkit.com",
    "description": "A Node.js playground for experimenting with JavaScript code."
  },
  {
    "title": "Scaleway",
    "url": "https://www.scaleway.com",
    "description": "A cloud computing platform offering scalable infrastructure solutions."
  },
  {
    "title": "Superhuman",
    "url": "https://superhuman.com",
    "description": "An advanced email management tool for professionals."
  },
  {
    "title": "Typora",
    "url": "https://typora.io",
    "description": "A minimal markdown editor for distraction-free writing."
  },
  {
    "title": "Unsplash",
    "url": "https://unsplash.com",
    "description": "A library of high-resolution, royalty-free images."
  },
  {
    "title": "WaniKani",
    "url": "https://www.wanikani.com",
    "description": "A Japanese learning tool focused on kanji and vocabulary."
  },

]
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "").strip().lower()
    if not query:
        return jsonify([])

    results = [item for item in search_data if query in item["title"].lower() or query in item["description"].lower()]
    return jsonify(results)

if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    app.run(debug=True, host="0.0.0.0", port=5000)
