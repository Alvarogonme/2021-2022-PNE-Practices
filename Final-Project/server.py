import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import jinja2 as j
import http.client
import json
from Seq1 import Seq
from http import HTTPStatus


SERVER = "rest.ensembl.org"
PORT = 20500

genes_list = {"FRAT1": "ENSG00000165879",
         "ADA": "ENSG00000196839",
         "FXN": "ENSG00000165060",
         "RNU6_269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552",
         "TTTY4C": "ENSG00000228296",
         "RBMY2YP": "ENSG00000227633",
         "FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052",
         "ANK2": "ENSG00000145362"}

names = genes_list.keys()
NAMES_LIST = []
for n in names:
    NAMES_LIST.append(n)


def read_html_file(filename):
    contents = Path("./html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

def read_template_html_file(filename):
    import jinja2
    from pathlib import Path
    content = jinja2.Template(Path(filename).read_text())
    return content


def connection_request(endpoint, params=""):
    conn = http.client.HTTPConnection(SERVER)
    parameters = "?content-type=application/json"
    try:
        conn.request("GET", endpoint + parameters + params)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data2 = json.loads(data1)
    return data2

def count_bases(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:
        d[b] += 1

    total = sum(d.values())
    for k, v in d.items():
        d[k] = [v, round((v * 100) / total, 2)]
    return d


socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        parsed_url = urlparse(self.path)  # path = url
        path = parsed_url.path
        params = parse_qs(parsed_url.query)
        print(f"Endpoints: {path}, Parameters: {params}")

        if path == "/":
            contents = Path("html/index.html").read_text()
            self.send_response(200)
        elif path == "/listSpecies":
            dict_1 = connection_request("/info/species", "")
            dict_2 = dict_1["species"]
            total = len(dict_2)
            try:
                if len(params) == 1:
                    limit = int(params['limit'][0])
                elif len(params) == 0:
                    limit = total
                else:
                    contents = read_html_file("Error.html"). \
                        render()

                species_list = []
                for element in range(0, limit):
                    species_list.append(dict_2[element]["common_name"])
                species = ""
                for element in species_list:
                    species += f"·{element.capitalize()}<br>"

                contents = read_html_file(path[1:] + ".html").\
                    render(context={"species": species,
                                    "total": total,
                                    "limit": limit})
            except Exception:
                contents = read_html_file("Error.html"). \
                    render()

        elif path == "/karyotype":
            try:
                specie = str(params['specie'][0].strip())
                dict_1 = connection_request("/info/assembly/" + specie, "")

                info_kar = dict_1["karyotype"]

                contents = read_html_file(path[1:] + ".html").\
                    render(context={'karyotype': info_kar})
            except KeyError:
                contents = read_html_file("Error.html"). \
                    render()

        elif path == "/chromosomeLength":
            try:
                if len(params) == 2:
                    specie_name = params['specie'][0]
                    number = params['chromo'][0]
                    dict_1 = connection_request("info/assembly/" + specie_name, "")
                    dict_2 = dict_1["top_level_region"]
                    length = 0

                    for e in range(0, len(dict_2)):
                        length += int(dict_2[e]["length"])

                        contents = read_html_file(path[1:] + ".html"). \
                            render(context={'length': length})

                else:
                    contents = read_html_file("Error.html"). \
                        render()

            except Exception:
                contents = read_html_file("Error.html"). \
                    render()

        elif path == "/geneSeq":
            try:
                gene = str(params['gene'][0].strip())
                key = genes_list[gene]
                dict_1 = connection_request("/sequence/id/" + str(key), "")
                sequence = dict_1["seq"]
                contents = read_html_file(path[1:] + ".html") \
                    .render(context={
                    "seq": sequence
                })

            except KeyError:
                contents = read_html_file("Error.html"). \
                    render()

        elif path == "/geneInfo":
            try:
                endpoint = '/sequence/id/'
                gene = params["gene"][0]
                if gene in genes_list.keys():
                    gene = genes_list[gene]

                dict_1 = connection_request(endpoint + gene)
                desc_dic = dict_1["desc"].split(":")
                contents = read_html_file("geneInfo.html").render(context={
                    "start": desc_dic[3],
                    "end": desc_dic[4],
                    "l": len(dict_1["seq"]),
                    "id": dict_1["id"],
                    "name": desc_dic[1]
                })
            except KeyError:
                contents = read_html_file("Error.html"). \
                    render()

        elif path == "/geneCalc":
            try:
                calc = params["gene"][0].strip()
                stable_id = genes_list[calc]
                dict_1 = connection_request("/sequence/id/" + stable_id, "")
                sequence= dict_1["seq"]
                s = Seq(sequence)
                print("dict:", dict_1)
                contents = read_html_file(path[1:] + ".html") \
                        .render(context={"length": s.len(), "bases": count_bases(sequence), "seq": calc})
            except KeyError:
                contents = read_html_file("Error.html") \
                        .render()

        elif path == "/geneList": #get/phenotype/region/:species/:region
            try:
                list = params["chromo"][0].strip()
                start = params["start"][0].strip()
                end = params["end"][0].strip()
                endpoint = list + ":" + start + "-" + end
                dict_1 = connection_request("/phenotype/region/homo_sapiens/" + endpoint, ";feature_type=Variation")
                list_genes = []
                try:
                    for d in dict_1:
                        for dict in d["phenotype_associations"]:
                            if "attributes" in dict:
                                if "associated_gene" in dict["attributes"]:
                                    list_genes.append(dict["attributes"]["associated_gene"])
                    print("list:", list_genes)
                    contents = read_html_file(path[1:] + ".html").render(context={"gene": list_genes})
                except TypeError:
                    contents = read_html_file("Error.html") \
                            .render()
            except KeyError:
                    contents = read_html_file("Error.html") \
                        .render()
        else:
            contents = read_html_file("Error.html"). \
                render()

        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return



with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT...", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Stopped by the user")
        httpd.server_close()