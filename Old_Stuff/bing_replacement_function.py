
def download_image(self, link, query):
        self.download_count += 1
        
        # Get the image link
        try:
            path = urllib.parse.urlsplit(link).path
            filename = posixpath.basename(path).split('?')[0]
            file_type = filename.split(".")[-1]

            # editied by ben
            ################################################################################

            if file_type in ['jpg','jpeg']:
                # download
                print("[%] Downloading Image #{} from {}".format(self.download_count, link))

                self.save_image(link, "{}/dataset/bing/{}/".format(os.getcwd(), query) + "Image_{}.{}".format(
                    str(self.download_count), file_type))
                print("[%] File Downloaded !\n")

            if file_type not  in ['jpg','jpeg']:
                #skip
                print('skipping {}'.format(file_type))
                self.download_count -= 1

            ################################################################################

        except Exception as e:
            self.download_count -= 1
            print("[!] Issue getting: {}\n[!] Error:: {}".format(link, e))
