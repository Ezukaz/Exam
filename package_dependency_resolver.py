def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    not_installed = [
        (name, [d for d in deps if d in packages])
        for name, deps in packages.items()
    ]
    output = []
    done = set()
    while not_installed:
        recycle = []
        installed = []
        for name, deps in not_installed:
            remaining = [d for d in deps if d not in done]
            if not remaining:
                installed.append(name)
            else:
                recycle.append((name, remaining))
        if not installed:
            return []
        installed.sort()
        output += installed
        done.update(installed)
        not_installed = recycle
    return output


print(package_dependency_resolver({"C": ["A", "B"], "A": [], "B": []}))
