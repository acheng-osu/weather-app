from search_by_zip import search_by_zip
import logging
import json

import grpc
import zip_pb2
import zip_pb2_grpc

def area_search():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = zip_pb2_grpc.ZipSearchingStub(channel)

        zipCodeInput = input("Please input your zip code here: ")
        radiusInput = int(input("Please input your radius here: "))
        responseString = stub.ZipSearching(zip_pb2.ZipInput(zipCode = zipCodeInput, radius=radiusInput))
        dumpableString = responseString.output.replace("'",'"')
        dumpableStringAsArray = json.loads(dumpableString)

        for zip in dumpableStringAsArray:
            print(search_by_zip(zip))




        # print(dumpableStringAsArray)
        # print(type(dumpableStringAsArray))

if __name__ == "__main__":
    area_search()