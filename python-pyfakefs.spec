%if 0%{?fedora}
%global with_python3 1
%endif
%global package_name pyfakefs

Name:           python-%{package_name}
Version:        3.1
Release:        1%{?dist}
Summary:        pyfakefs implements a fake file system that mocks the Python file system modules.
License:        ASL 2.0
URL:            http://pyfakefs.org
Source0:        https://pypi.io/packages/source/p/%{package_name}/%{package_name}-%{version}.tar.gz
BuildArch:      noarch


%description
pyfakefs implements a fake file system that mocks the Python file system
modules.
Using pyfakefs, your tests operate on a fake file system in memory without
touching the real disk. The software under test requires no modification to
work with pyfakefs.

%package -n python2-%{package_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{package_name}}

BuildRequires:  git
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

Requires:       python2-mox3 >= 0.10.0
Requires:       python2-pytest >= 2.8.6

%description -n python2-%{package_name}
pyfakefs implements a fake file system that mocks the Python file system
modules.
Using pyfakefs, your tests operate on a fake file system in memory without
touching the real disk. The software under test requires no modification to
work with pyfakefs.

%if 0%{?with_python3}
%package -n python3-%{package_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{package_name}}

BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-mox3 >= 0.10.0
Requires:       python3-pytest >= 2.8.6

%description -n python3-%{package_name}
pyfakefs implements a fake file system that mocks the Python file system
modules.
Using pyfakefs, your tests operate on a fake file system in memory without
touching the real disk. The software under test requires no modification to
work with pyfakefs.
%endif

%prep
%autosetup -n %{package_name}-%{version} -S git

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

%files -n python2-%{package_name}
%license COPYING
%doc README.md
%{python2_sitelib}/%{package_name}
%{python2_sitelib}/*.egg-info

%if 0%{?with_python3}
%files -n python3-%{package_name}
%license COPYING
%doc README.md
%{python3_sitelib}/%{package_name}
%{python3_sitelib}/*.egg-info
%endif # with_python3

%changelog
* Mon May 1 2017 David Moreau Simard <dmsimard@redhat.com> - 3.1-1
- First packaged version of pyfakefs
