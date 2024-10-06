from pymilvus import connections, utility, Collection

# 配置 Milvus 的连接信息
MILVUS_HOST = "localhost"  # 替换为你的 Milvus 实例的 IP 地址或主机名
MILVUS_PORT = "19530"      # 替换为你的 Milvus 实例的端口

def list_all_collections():
    # 连接到 Milvus
    connections.connect("default", host=MILVUS_HOST, port=MILVUS_PORT)
    
    # 获取所有的 collection 名称
    collections = utility.list_collections()
    
    if collections:
        print(f"Collections in Milvus: {collections}")
    else:
        print("No collections found in Milvus.")
    
    # 断开连接
    connections.disconnect("default")
def delete_collection(collection_name):
    # 连接到 Milvus
    connections.connect("default", host=MILVUS_HOST, port=MILVUS_PORT)

    # 检查 collection 是否存在
    if Collection.exists(collection_name):
        # 删除 collection
        collection = Collection(collection_name)
        collection.drop()
        print(f"Collection '{collection_name}' has been deleted.")
    else:
        print(f"Collection '{collection_name}' does not exist.")

    # 断开连接
    connections.disconnect("default")

if __name__ == "__main__":
    # 要删除的 collection 名称
    collection_name_to_delete = "knowledgeBase"  # 替换为要删除的 collection 名称
    delete_collection(collection_name_to_delete)

