class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = collections.defaultdict(int)
        result = []

        for dom in cpdomains:
            dom_list = dom.split()
            visits, dom_str = int(dom_list[0]), dom_list[1]
            
            single_doms = dom_str.split('.')
            while single_doms:
                counter[".".join(single_doms)] += visits
                single_doms = single_doms[1:]

        for key,val in counter.items():
            result.append(f"{val} {key}")
        return result
