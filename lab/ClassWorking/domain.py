# Tracks frequency of domains in web searches
import web_search  # Causes unintended search

domains = {}

terms = input("\nEnter search terms ('q' to quit): ")
while terms != 'q':
    results = web_search.search(terms)

    for link in results:
        if '.com' in link:
            domain_end = link.find('.com')
        elif '.net' in link:
            domain_end = link.find('.net')
        elif '.org' in link:
            domain_end = link.find('.org')
        else:
            print('Unknown top level domain')
            continue

        dom = link[:domain_end + 4]
        if dom not in domains:
            domains[dom] = 1
        else:
            domains[dom] += 1

    terms = input("Enter search terms ('q' to quit): ")

print('\nNumber of search results for each site:')
for domain, num in domains.items():
    print(domain + ':', num)