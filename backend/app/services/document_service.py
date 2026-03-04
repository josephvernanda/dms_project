def request_delete(db, doc, user_id):
    if doc.status != DocumentStatus.ACTIVE:
        raise Exception("Document not active")

    doc.status = DocumentStatus.PENDING_DELETE

    permission = PermissionRequest(
        document_id=doc.id,
        type=PermissionType.DELETE,
        requested_by=user_id
    )

    db.add(permission)
    db.commit()
    return permission