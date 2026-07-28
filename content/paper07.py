from ._model import P, Q

PAPER = {
    'number': 7,
    'title': 'The nature of marketing',
    'theme': 'Syllabus 3.1 \u2013 Marketing objectives, demand and supply, types of market, mass and niche marketing, segmentation and customer relationship marketing.',
    'time': '1 hour 45 minutes',
    'sectionA': [
        Q([
            P('a', 'Define \u2018marketing objective\u2019.', 2, ['A specific marketing goal a business wants to achieve (1), e.g. to raise market share or brand awareness, that supports corporate objectives (1).']),
            P('b', 'Explain the link between marketing objectives and corporate objectives.', 5, [
                'Corporate objectives (e.g. growth) set the overall direction.',
                'Marketing objectives (e.g. +10% market share) are derived to help achieve them.',
                'They must be consistent so marketing activity supports overall strategy.',
                'Up to 5 for developed explanation.',
            ]),
        ]),
        Q([
            P('a', 'State two factors that influence the demand for a product.', 2, ['Any two: price, incomes, price of substitutes/complements, tastes/fashion, advertising, season, population.']),
            P('b', 'Explain how a rise in consumer incomes could affect demand for a luxury car.', 4, ['Luxury cars are a normal/luxury good, so higher incomes raise demand (shift right); consumers can afford more premium goods. 1\u20132 + development.']),
        ]),
        Q([
            P('a', 'Explain how the interaction of demand and supply determines the market price.', 4, [
                'Price settles at equilibrium where quantity demanded = quantity supplied.',
                'Excess demand pushes price up; excess supply pushes it down until they balance.',
            ]),
            P('b', 'Draw and label a demand and supply diagram showing equilibrium price and quantity.', 3, ['Axes: price (y), quantity (x); downward demand, upward supply; intersection marked P and Q. 3 marks for correct, labelled diagram.'],
              ),
        ], diagram={'type': 'demand_supply', 'caption': 'Fig: Draw a diagram like this and label equilibrium P and Q'}),
        Q([
            P('a', 'Distinguish between a consumer market and an industrial market.', 4, [
                'Consumer (B2C): goods/services sold to households for personal use (2).',
                'Industrial (B2B): goods/services sold to other businesses for use in production (2).',
            ]),
            P('b', 'Explain one way marketing differs between B2C and B2B.', 3, ['B2B: fewer, larger buyers, relationship/technical selling, negotiated prices; B2C: mass promotion, branding, emotional appeal. 1 + 2.']),
        ]),
        Q([
            P('a', 'Define \u2018market share\u2019.', 2, ['The proportion of total sales in a market (by value or volume) held by one business/product (1), usually expressed as a percentage (1).']),
            P('b', 'A firm sells $6m in a market worth $40m. Calculate its market share and explain one implication of a rising share.', 5, [
                '=Market share = (6 / 40) \u00d7 100 = 15%',
                'Rising share suggests growing competitiveness/brand strength, possible economies of scale and market power.',
                '2 calc + up to 3 explanation.',
            ]),
        ]),
        Q([
            P('a', 'Distinguish between mass marketing and niche marketing.', 4, [
                'Mass: aiming a product at the whole/large market with a standardised offer (2).',
                'Niche: targeting a small, specific segment with a specialised offer (2).',
            ]),
            P('b', 'Explain one advantage of niche marketing for a small business.', 3, ['Less direct competition from large firms, can charge premium prices, closer customer relationships, lower marketing spend. 1 + 2.']),
        ]),
        Q([
            P('a', 'State the three main methods of market segmentation.', 3, ['Geographic (1), demographic (1) and psychographic (1) (accept behavioural).']),
            P('b', 'Analyse two benefits to a business of segmenting its market.', 6, [
                'Targets marketing more precisely -> higher response/lower waste.',
                'Tailors product/price to segment needs -> higher satisfaction and possibly premium prices.',
                'Identifies gaps/new segments; improves customer retention.',
                'L|Level 2 (4-6)|Two benefits analysed with development.',
                'L|Level 1 (1-3)|Identifies benefits, limited development.',
            ]),
        ]),
        Q([
            P('a', 'Define \u2018customer relationship marketing (CRM)\u2019.', 3, ['A strategy focused on building long-term relationships with customers (1) to increase loyalty and repeat purchases (1) rather than one-off sales (1).']),
            P('b', 'Explain one cost and one benefit of CRM.', 4, ['Benefit: loyalty/repeat sales, higher lifetime value, referrals. Cost: technology/CRM systems, staff time, data management. 2 each.']),
        ]),
        Q([
            P('a', 'Distinguish between product orientation and market (customer) orientation.', 4, [
                'Product-orientated: focuses on the product/what the firm can make (2).',
                'Market-orientated: focuses on identifying and meeting customer needs (2).',
            ]),
            P('b', 'Explain one risk of being product-orientated.', 3, ['May produce goods customers do not want -> unsold stock/lost sales; ignores changing tastes. 1 + 2.']),
        ]),
        Q([
            P('a', 'Define \u2018market growth\u2019.', 2, ['The increase in the total size/sales of a market over a period (1), usually shown as a percentage change (1).']),
            P('b', 'Analyse the implications for a business of operating in a rapidly growing market.', 6, [
                'Opportunity for higher sales/economies of scale and new customers.',
                'But attracts new competitors; needs investment/capacity; risk of overtrading.',
                'L|Level 2 (4-6)|Developed analysis of implications.',
                'L|Level 1 (1-3)|States implications, limited development.',
            ]),
        ]),
    ],
    'sectionB': [
        Q([
            P('a', 'Analyse how market segmentation could help a clothing retailer increase sales.', 8, [
                'Identify segments (age, income, lifestyle) and tailor ranges/prices to each.',
                'Target promotion to the right audience -> higher conversion and loyalty.',
                'Spot underserved segments/new opportunities.',
                'L|Level 3 (6-8)|Developed, applied analysis.', 'L|Level 2 (3-5)|Some.',
                'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', 'Evaluate whether niche marketing or mass marketing is the better strategy for a new food producer.', 12, [
                'Niche: less competition, premium prices, loyal customers, lower initial spend; but small sales, vulnerable if segment shrinks or a big firm enters.',
                'Mass: high volume, economies of scale, brand reach; but heavy competition/spend and needs large capacity/finance.',
                'Judgement: for a new/small producer niche is usually safer initially; depends on finance, capacity and product. Could grow niche -> mass later.',
                'L|Level 4 (10-12)|Balanced, supported judgement, contextual.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
        Q([
            P('a', 'Analyse how a business could become more market-orientated.', 8, [
                'Conduct market research to identify customer needs and monitor trends.',
                'Involve marketing in product development; use customer feedback/CRM data.',
                'Adjust the marketing mix to match customer wants.',
                'L|Level 3 (6-8)|Developed analysis.', 'L|Level 2 (3-5)|Some.',
                'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', 'Evaluate the view that customer relationship marketing is worth the investment for all businesses.', 12, [
                'For: loyalty, repeat purchase, higher lifetime value, cheaper than winning new customers, referrals, useful data.',
                'Against: costly systems/time; low value for one-off/low-frequency purchases; data/privacy risks; not all customers want a \u2018relationship\u2019.',
                'Judgement: worthwhile where repeat purchase and customer lifetime value are high (e.g. banking, subscriptions); less so for infrequent low-value goods.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
        Q([
            P('a', 'Analyse how changes in supply and demand could affect the price and sales of coffee for a cafe chain.', 8, [
                'A poor harvest cuts supply of beans -> input prices rise -> higher costs/prices.',
                'A health trend or rising incomes raises demand -> higher prices/sales.',
                'The chain must respond via pricing/menu decisions.',
                'L|Level 3 (6-8)|Developed analysis using demand/supply.',
                'L|Level 2 (3-5)|Some.', 'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', 'Evaluate the importance of setting SMART marketing objectives for a business launching a new product.', 12, [
                'For: focus, coordination, measurement, motivation, benchmark to judge the launch.',
                'Against: uncertain new markets make realistic targets hard; rigid objectives may not adapt; success also depends on execution and rivals.',
                'Judgement: valuable for control but must be flexible/reviewed; important yet not sufficient on its own.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
        Q([
            P('a', 'Analyse why a growing market share can benefit a business.', 8, [
                'Higher sales/revenue and economies of scale lowering unit costs.',
                'Greater market power/brand strength, bargaining power with suppliers/retailers.',
                'Can support price leadership and deter entrants.',
                'L|Level 3 (6-8)|Developed analysis.', 'L|Level 2 (3-5)|Some.',
                'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', '\u2018Understanding customers is more important than beating competitors.\u2019 Evaluate this view for a marketing manager.', 12, [
                'For customers: needs-led (market orientation) drives loyalty, retention and the right products; source of long-term success.',
                'For competitors: must monitor rivals to remain competitive on price/features and defend share.',
                'Judgement: both matter and interlink; deep customer understanding usually the foundation, but ignoring competitors is dangerous. Depends on market rivalry.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
    ],
    'case': {
        'title': 'BrightBrew targets a niche',
        'context': [
            'BrightBrew is a small producer of premium, ethically sourced coffee pods aimed at higher-income, environmentally conscious consumers \u2013 a niche it has served profitably for three years. The market for coffee pods is growing at 12% per year but is dominated by two large firms using mass marketing. BrightBrew builds strong relationships with customers through a subscription service and personalised recommendations.',
            'A global recession has squeezed consumer incomes and a bean shortage has raised BrightBrew\u2019s costs. The founders are considering two moves: (a) broaden into mass-market, cheaper pods sold through supermarkets, or (b) invest further in CRM and its premium niche. They must decide how to segment and target the market.',
        ],
        'exhibits': [
            {'type': 'table', 'title': 'Table 1: BrightBrew market data',
             'headers': ['Measure', 'Value'],
             'rows': [['BrightBrew annual sales', '$3.1m'],
                      ['Total pod market size', '$260m'],
                      ['Market growth (per year)', '12%'],
                      ['Repeat-purchase (subscription) rate', '68%'],
                      ['Average customer income', 'top 20%']],
             'col_w': [3, 1], 'align': ['left', 'right']},
            {'type': 'diagram', 'name': 'demand_supply',
             'caption': 'Fig 1: A bean shortage shifts supply, raising input prices'},
        ],
        'questions': [
            Q([P('', 'Define the term \u2018niche market\u2019.', 2, ['A small, specific segment of a larger market with particular needs (2).'])]),
            Q([P('', 'Using Table 1, calculate BrightBrew\u2019s market share.', 3, [
                '=Market share = (3.1 / 260) \u00d7 100 \u2248 1.2%',
                '2 method + 1 answer (\u22481.2%).',
            ])]),
            Q([P('', 'Identify the segmentation base BrightBrew mainly uses, and justify your answer.', 3, ['Demographic/psychographic (1) \u2013 targets high-income (top 20%) and environmentally conscious/lifestyle consumers (2).'])]),
            Q([P('', 'Explain how the bean shortage (Fig 1) is likely to affect BrightBrew\u2019s costs and pricing.', 4, [
                'Reduced supply raises the market price of beans -> higher input costs.',
                'BrightBrew may raise prices (premium buyers less price-sensitive) or absorb costs, cutting margins.',
                '1\u20132 use of diagram + 2 development.',
            ])]),
            Q([P('', 'Analyse the benefits to BrightBrew of its customer relationship marketing.', 8, [
                'High repeat-purchase (68%) via subscription -> stable revenue and high customer lifetime value.',
                'Personalisation raises satisfaction/loyalty and word-of-mouth, defending its niche against big rivals.',
                'Customer data guides product/marketing decisions.',
                'L|Level 3 (6-8)|Developed analysis using case data.',
                'L|Level 2 (3-5)|Some.', 'L|Level 1 (1-2)|Identification.',
            ])]),
            Q([P('', 'Recommend whether BrightBrew should move into the mass market or stay in its premium niche. Justify your recommendation.', 12, [
                '#For mass market', 'Access to a large, growing ($260m, +12%) market and economies of scale; recession makes cheaper pods attractive.',
                '#For staying niche', 'Head-to-head competition with two dominant mass firms is risky/costly; would dilute its ethical premium brand and lose its 68% loyalty; premium buyers are less hit by recession.',
                '#Judgement', 'Supported recommendation, e.g. remain in and deepen the profitable niche via CRM (its core strength) rather than compete on price with giants; perhaps a limited premium supermarket range rather than full mass market. Weigh brand identity vs scale.',
                'L|Level 4 (10-12)|Balanced, uses data, justified recommendation.',
                'L|Level 3 (7-9)|Balanced, some judgement/application.',
                'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided/assertion.',
            ])]),
        ],
    },
}
