#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC36CDCB4DF00C68C (infra-root@openstack.org)
#
Name     : oslo.middleware
Version  : 3.36.0
Release  : 53
URL      : https://tarballs.openstack.org/oslo.middleware/oslo.middleware-3.36.0.tar.gz
Source0  : https://tarballs.openstack.org/oslo.middleware/oslo.middleware-3.36.0.tar.gz
Source99 : https://tarballs.openstack.org/oslo.middleware/oslo.middleware-3.36.0.tar.gz.asc
Summary  : Oslo Middleware library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.middleware-python3
Requires: oslo.middleware-license
Requires: oslo.middleware-python
Requires: Jinja2
Requires: Sphinx
Requires: WebOb
Requires: debtcollector
Requires: fixtures
Requires: oslo.config
Requires: oslo.context
Requires: oslo.i18n
Requires: oslo.utils
Requires: pbr
Requires: reno
Requires: six
Requires: stevedore
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
oslo.middleware
        ===================================

%package license
Summary: license components for the oslo.middleware package.
Group: Default

%description license
license components for the oslo.middleware package.


%package python
Summary: python components for the oslo.middleware package.
Group: Default
Requires: oslo.middleware-python3

%description python
python components for the oslo.middleware package.


%package python3
Summary: python3 components for the oslo.middleware package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oslo.middleware package.


%prep
%setup -q -n oslo.middleware-3.36.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532269355
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/oslo.middleware
cp LICENSE %{buildroot}/usr/share/doc/oslo.middleware/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/oslo.middleware/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
