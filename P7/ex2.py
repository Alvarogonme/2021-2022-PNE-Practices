# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json

genes_dict = {"SRCAP": "ENSG00000080603",
              "FRAT1": "ENSG00000165879",
              "ADA": "ENSG00000196839",
              "FXN": "ENSG00000165060",
              "RNU6_269P": "ENSG00000212379",
              "MIR633": "ENSG00000207588",
              "TTTY4C": "ENSG00000228296",
              "RBMY2YP": "ENSG00000227633",
              "FGFR3": "ENSG00000068078",
              "KDR": "ENSG00000128052",
              "ANK2": "ENSG00000145362"}

print('Dictionary of genes!' "\n"
      'There are 10 genes in the dicctionary:'"\n")

for k,v in genes_dict.items():
    print(f"{k} --> {v}")


