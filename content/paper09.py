from ._model import P, Q

PAPER = {
    'number': 9,
    'title': 'The marketing mix: portfolio, price, promotion & place',
    'theme': 'Syllabus 3.3.3\u20133.3.6 \u2013 Product life cycle, Boston Matrix, pricing methods, promotion (including digital), branding, packaging and channels of distribution.',
    'time': '1 hour 45 minutes',
    'sectionA': [
        Q([
            P('a', 'Define \u2018product life cycle\u2019.', 2, ['The stages a product passes through over time \u2013 development, introduction, growth, maturity and decline (1) \u2013 shown by sales over time (1).']),
            P('b', 'Explain two extension strategies a business could use to prolong the maturity stage.', 6, [
                'New uses/markets; restyling or new features/variants.',
                'New packaging, increased promotion, price changes, targeting new segments.',
                '#Marks', 'Up to 3 per strategy (identification + development).',
            ]),
        ], diagram={'type': 'plc', 'caption': 'Fig: The product life cycle (sketch it and label the stages)'}),
        Q([
            P('a', 'State the four categories of the Boston Matrix.', 2, ['Star, Question mark (problem child), Cash cow, Dog (all four for 2).']),
            P('b', 'Analyse how the Boston Matrix can help a business manage its product portfolio.', 6, [
                'Identifies which products to invest in (stars), harvest for cash (cash cows), review (question marks) or drop (dogs).',
                'Guides balanced portfolio and cash allocation (cash cows fund stars).',
                'L|Level 2 (4-6)|Developed analysis of portfolio decisions.',
                'L|Level 1 (1-3)|Describes categories, limited analysis.',
            ]),
        ], diagram={'type': 'boston', 'caption': 'Fig: The Boston Matrix'}),
        Q([
            P('a', 'Define \u2018penetration pricing\u2019.', 2, ['Setting a low initial price to enter a market/gain market share quickly (1), then possibly raising it later (1).']),
            P('b', 'Explain a situation where penetration pricing would be appropriate.', 4, ['A new product entering a competitive mass market with price-sensitive buyers, aiming for volume/market share. 1\u20132 + development.']),
        ]),
        Q([
            P('a', 'Define \u2018price skimming\u2019.', 2, ['Setting a high initial price for a new/innovative product (1) to maximise revenue from early adopters before lowering it (1).']),
            P('b', 'Explain why skimming might suit a new technology product.', 4, ['Little competition initially, early adopters pay a premium, recovers R&D quickly; price falls as rivals enter. 1\u20132 + development.']),
        ]),
        Q([
            P('a', 'Define \u2018dynamic pricing\u2019.', 3, ['Adjusting prices in real time (1) in response to demand, timing or customer data (1), e.g. airline/ride-hailing prices (1).']),
            P('b', 'Explain one risk of using dynamic pricing.', 3, ['Customers may feel exploited/unfair -> reputation damage; complexity; needs data/systems. 1 + 2.']),
        ]),
        Q([
            P('a', 'Distinguish between cost-based pricing and competitive pricing.', 4, [
                'Cost-based: price set by adding a mark-up to unit cost (2).',
                'Competitive: price set in line with/relative to competitors\u2019 prices (2).',
            ]),
            P('b', 'Explain one limitation of cost-based pricing.', 3, ['Ignores demand/what customers will pay and competitors; may price too high (lose sales) or too low (lose profit). 1 + 2.']),
        ]),
        Q([
            P('a', 'State two objectives of promotion.', 2, ['Any two: inform, persuade, remind, build brand/loyalty, increase sales/market share, launch a product.']),
            P('b', 'Analyse the growing importance of digital promotion for businesses.', 6, [
                'Wide, targeted reach at lower cost; measurable (analytics); interactive/social.',
                'Personalisation and remarketing; supports e-commerce; but oversupply of ads/ad-blocking and reputation risk.',
                'L|Level 2 (4-6)|Developed analysis of digital promotion.',
                'L|Level 1 (1-3)|States points, limited development.',
            ]),
        ]),
        Q([
            P('a', 'Explain the role of branding in promotion.', 4, ['Builds recognition, trust and loyalty; differentiates; supports premium pricing and repeat purchase. 1\u20132 + development.']),
            P('b', 'Explain the role of packaging in promotion.', 3, ['Attracts attention, communicates brand/information, protects product, can be a USP/differentiator. 1 + 2.']),
        ]),
        Q([
            P('a', 'Distinguish between digital and physical distribution channels.', 4, [
                'Physical: goods reach customers through wholesalers/retailers/physical stores (2).',
                'Digital: products/services delivered or sold online (e-commerce, downloads/streaming) (2).',
            ]),
            P('b', 'Explain one benefit to a manufacturer of selling directly to consumers online.', 3, ['Higher margins (no intermediary), direct customer data/relationship, control of brand. 1 + 2.']),
        ]),
        Q([
            P('a', 'Define \u2018price discrimination\u2019.', 2, ['Charging different prices to different customers/segments for the same product (1) based on their willingness/ability to pay (1).']),
            P('b', 'Explain one example of psychological pricing and why it works.', 4, ['Pricing at $9.99 rather than $10 makes it seem cheaper (left-digit effect), encouraging purchase. 1\u20132 + development.']),
        ]),
    ],
    'sectionB': [
        Q([
            P('a', 'Analyse how a business could use the product life cycle to plan its marketing.', 8, [
                'Different mix at each stage: heavy promotion/skimming or penetration at introduction; build distribution in growth.',
                'Extension strategies in maturity; harvest/withdraw in decline.',
                'Manage a portfolio so new products replace declining ones.',
                'L|Level 3 (6-8)|Developed, applied analysis.', 'L|Level 2 (3-5)|Some.',
                'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', 'Evaluate whether penetration pricing is the best strategy for launching a new product in a competitive market.', 12, [
                'For: gains share/volume quickly, deters entrants, economies of scale, suits price-sensitive mass market.',
                'Against: low margins/slow payback, may signal low quality, hard to raise price later, price war risk; skimming/competitive/value pricing may suit innovative or premium products.',
                'Judgement: best where the market is price-sensitive and scale matters; not best for differentiated/innovative goods. Depends on product and rivals.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
        Q([
            P('a', 'Analyse the factors a business should consider when choosing a channel of distribution.', 8, [
                'Nature of product (perishable, technical, bulky), target market and their buying habits.',
                'Cost/margin, control of brand, reach/coverage, competitors\u2019 channels.',
                'Digital capability and speed.',
                'L|Level 3 (6-8)|Developed analysis.', 'L|Level 2 (3-5)|Some.',
                'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', 'Evaluate the view that digital promotion has made traditional advertising unnecessary.', 12, [
                'For digital: cheaper, targeted, measurable, interactive, growing reach, essential for e-commerce.',
                'Against: traditional (TV, print, outdoor) still reaches mass/older audiences, builds brand, high trust; ad-blocking/fraud online; best mix depends on audience.',
                'Judgement: digital is dominant and growing but not a total replacement; an integrated mix is usually best. Depends on target market and budget.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
        Q([
            P('a', 'Analyse how strong branding can benefit a business.', 8, [
                'Recognition, trust and loyalty -> repeat purchase and premium pricing.',
                'Easier launch of new products (brand extension); differentiation; bargaining power with retailers.',
                'L|Level 3 (6-8)|Developed analysis.', 'L|Level 2 (3-5)|Some.',
                'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', '\u2018The product is the most important element of the marketing mix.\u2019 Evaluate this view.', 12, [
                'For product: without a good product meeting needs, price/promotion/place cannot succeed; USP drives everything.',
                'Against: a great product fails with wrong price, poor promotion or unavailability; the Ps are interdependent; in some markets price/place dominate.',
                'Judgement: product is fundamental but not sufficient; the whole, consistent mix matters. Importance varies by market.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
        Q([
            P('a', 'Analyse how a business could use the Boston Matrix to make marketing decisions.', 8, [
                'Invest in stars (high growth, high share) to become future cash cows.',
                'Use cash-cow revenue to fund stars/question marks; decide which question marks to back or drop.',
                'Divest dogs; aim for a balanced portfolio.',
                'L|Level 3 (6-8)|Developed, applied analysis.', 'L|Level 2 (3-5)|Some.',
                'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', 'Evaluate the usefulness of the product life cycle model for making marketing decisions.', 12, [
                'For: guides mix changes, extension strategies and portfolio planning; simple/widely used.',
                'Against: hard to know the current stage; not all products follow the curve (fads, classics); length of stages varies; can become self-fulfilling if withdrawal is premature.',
                'Judgement: a useful planning tool if used flexibly alongside data, not a precise predictor. Depends on product/market.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
    ],
    'case': {
        'title': 'Aurora Electronics rebalances its portfolio',
        'context': [
            'Aurora Electronics sells four product lines. Its long-running \u2018ClassicPhone\u2019 has high market share but the smartphone market is now barely growing; it still generates strong cash. Its new \u2018FoldX\u2019 has a small share in a fast-growing foldable-phone market. A smart-watch has high share in a booming wearables market, while an old MP3 player has low share in a shrinking market.',
            'Marketing must decide pricing and promotion for the FoldX launch and how to manage the portfolio. Options for FoldX include price skimming (it has patented technology) or penetration pricing to build share fast. The finance director wants cash generated by ClassicPhone reinvested wisely.',
        ],
        'exhibits': [
            {'type': 'table', 'title': 'Table 1: Aurora product portfolio',
             'headers': ['Product', 'Market growth', 'Relative market share'],
             'rows': [['ClassicPhone', 'Low', 'High'],
                      ['FoldX', 'High', 'Low'],
                      ['Smart-watch', 'High', 'High'],
                      ['MP3 player', 'Low', 'Low']],
             'col_w': [2, 1.4, 1.6], 'align': ['left', 'center', 'center']},
            {'type': 'diagram', 'name': 'boston', 'caption': 'Fig 1: Place each Aurora product in the Boston Matrix'},
        ],
        'questions': [
            Q([P('', 'Define the term \u2018product portfolio\u2019.', 2, ['The range/collection of products a business sells (1) across different markets/segments (1).'])]),
            Q([P('', 'Using Table 1, classify each of the four products using the Boston Matrix.', 4, [
                'ClassicPhone = Cash cow (low growth, high share).',
                'FoldX = Question mark (high growth, low share).',
                'Smart-watch = Star (high growth, high share).',
                'MP3 player = Dog (low growth, low share).',
                '1 mark each.',
            ])]),
            Q([P('', 'Explain why ClassicPhone is described as generating \u2018strong cash\u2019 despite low market growth.', 4, [
                'High share in a mature market gives high sales with low investment need (no growth to fund).',
                'Established product, economies of scale, low promotion cost -> net cash inflow (cash cow).',
                '1\u20132 + development.',
            ])]),
            Q([P('', 'Analyse whether price skimming or penetration pricing is more suitable for the FoldX launch.', 6, [
                'Skimming: patented technology, few competitors, early adopters pay premium, recovers R&D.',
                'Penetration: builds share fast in a high-growth market but sacrifices margin and may not suit a premium/innovative product.',
                'L|Level 2 (4-6)|Weighs both using the case.',
                'L|Level 1 (1-3)|States methods, limited application.',
            ])]),
            Q([P('', 'Analyse how Aurora could use the cash from ClassicPhone to strengthen its portfolio.', 8, [
                'Reinvest in the star (smart-watch) and question mark (FoldX) to build/keep share in growing markets.',
                'Fund R&D/promotion so FoldX becomes a future star; consider dropping the MP3 dog.',
                'Balances the portfolio for long-term revenue as ClassicPhone eventually declines.',
                'L|Level 3 (6-8)|Developed analysis using Boston logic and the case.',
                'L|Level 2 (3-5)|Some.', 'L|Level 1 (1-2)|Identification.',
            ])]),
            Q([P('', 'Recommend a marketing strategy for FoldX, including pricing and promotion. Justify your recommendation using the case.', 12, [
                '#Pricing', 'Skimming suits its patented tech and premium positioning; lower later as rivals enter.',
                '#Promotion', 'Digital and targeted launch to early adopters/tech enthusiasts; stress USP (foldable innovation).',
                '#Portfolio link', 'Fund the launch from ClassicPhone cash; aim to convert the question mark into a star in the high-growth market.',
                '#Judgement', 'Supported recommendation weighing margin vs share; e.g. skim initially to fund investment and signal premium quality, then reduce price to build share as the market grows. Acknowledge risk of rivals/patents expiring.',
                'L|Level 4 (10-12)|Balanced, uses case, justified recommendation across the mix.',
                'L|Level 3 (7-9)|Balanced, some judgement/application.',
                'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided/assertion.',
            ])]),
        ],
    },
}
