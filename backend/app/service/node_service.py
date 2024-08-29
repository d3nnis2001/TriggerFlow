from ..repository.nodeRepository import NodeRepository

class NodeService:
    @staticmethod
    def upload_data(files):
        try:
            for file in files:
                file_content = file.read()
                filename = file.filename
                NodeRepository.upload_form_data(filename, file_content)
        except Exception as e:
            raise Exception(f"Error uploading files: {str(e)}")