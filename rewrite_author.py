import git_filter_repo as fr

def update_author(commit):
    if commit.author_email == b"d.aaid@univ-batna2.dz":
        commit.author_name = b"houssemkessouar-byte"
        commit.author_email = b"houssem.kessouar@etu.univ-batna2.dz"
        commit.committer_name = b"houssemkessouar-byte"
        commit.committer_email = b"houssem.kessouar@etu.univ-batna2.dz"

fr.RepoFilter(commit_callback=update_author).run()
