%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global library ovsdbapp
%global module ovsdbapp

%global common_desc \
A library for writing Open vSwitch OVSDB-based applications.

%global common_desc_tests \
Python OVSDB Application Library tests. \
This package contains Python OVSDB Application Library test files.

%if 0%{?el8} || 0%{?redos}
%global el_python3_pkgversion 3
%else
%global el_python3_pkgversion 36
%endif

%bcond_with tests

Name:       python-%{library}
Version:    2.5.0
Release:    1.ROCKIT4@BUILDID@%{?dist}
Summary:    Python OVSDB Application Library
License:    ASL 2.0
URL:        http://launchpad.net/%{library}/

Source0:    http://tarballs.openstack.org/%{library}/%{library}-%{upstream_version}.tar.gz

BuildArch:  noarch

BuildRequires:  git

%package -n python3-%{library}
Summary:    Python OVSDB Application Library
Requires:   python3-openvswitch
Requires:   python%{el_python3_pkgversion}-pbr
Requires:   python%{el_python3_pkgversion}-netaddr >= 0.7.18
Obsoletes:  python36-ovsdbapp < %{version}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{el_python3_pkgversion}-pbr
BuildRequires:  python%{el_python3_pkgversion}-mock
BuildRequires:  python%{el_python3_pkgversion}-netaddr >= 0.7.18
BuildRequires:  python3-openvswitch

%description -n python3-%{library}
%{common_desc}


%description
%{common_desc}


%prep
# Required for tarball sources verification
%autosetup -n %{library}-%{upstream_version} -S git -p 1


%build
%{py3_build}


%install
%{py3_install}


%files -n python3-%{library}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-*.egg-info
%exclude %{python3_sitelib}/%{module}/tests

%if 0%{?with_doc}
%files -n python-%{library}-doc
%doc doc/build/html
%license LICENSE
%endif


%changelog
* Mon Aug 16 2021 Vladislav Odintsov <odivlad@gmail.com> 1.11.0-1
- Adopt to CROC Cloud build processes

* Mon Nov 09 2020 RDO <dev@lists.rdoproject.org> 1.6.0-1
- Update to 1.6.0

* Wed Oct 21 2020 Joel Capitao <jcapitao@redhat.com> 1.5.0-2
- Enable sources tarball validation using GPG signature.

* Fri Sep 18 2020 RDO <dev@lists.rdoproject.org> 1.5.0-1
- Update to 1.5.0

