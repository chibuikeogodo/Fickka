function commentReplyToggle(parent_id) {
    cont row = document.getElementById(parent_id);

    if (row.classlist.contains('d-none')){
        row.classlist.remove('d-none');
    }else {
        row.classlist.add('d-none');
    }
}